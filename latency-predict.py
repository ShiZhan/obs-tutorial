import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.preprocessing import MinMaxScaler
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.metrics import mean_squared_error

# Load latencies data from CSV
latencies = pd.read_csv('latency.csv', header=None).values.flatten()

# Simulate timeline
timeline = []
current_time = 0
for latency in latencies:
    current_time += latency
    timeline.append(current_time)

# Define bin size (10 ms)
bin_size = 10

# Create bins
max_time = max(timeline)
bins = np.arange(0, max_time + bin_size, bin_size)

# Count requests in each bin
request_counts, _ = np.histogram(timeline, bins=bins)

# Now `request_counts` is the time series you can use for prediction
print(request_counts)

# Split data into training and testing sets
train_size = int(len(request_counts) * 0.8)
train, test = request_counts[:train_size], request_counts[train_size:]

# Function to create sequences for RNN models
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i + seq_length])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

# Prepare data for ARIMA
def arima_predict(train, test):
    model = ARIMA(train, order=(5, 1, 0))  # ARIMA(p, d, q)
    model_fit = model.fit()
    predictions = model_fit.forecast(steps=len(test))
    return predictions

# Prepare data for GRU and LSTM
seq_length = 10  # Sequence length for RNN models
X_train, y_train = create_sequences(train, seq_length)
X_test, y_test = create_sequences(test, seq_length)

# Normalize input features (X)
scaler_X = MinMaxScaler()
X_train = scaler_X.fit_transform(X_train)
X_test = scaler_X.transform(X_test)

# Normalize target (y) separately
scaler_y = MinMaxScaler()
y_train = scaler_y.fit_transform(y_train.reshape(-1, 1)).flatten()
y_test = scaler_y.transform(y_test.reshape(-1, 1)).flatten()

# Convert to PyTorch tensors
X_train = torch.tensor(X_train, dtype=torch.float32).unsqueeze(-1)
y_train = torch.tensor(y_train, dtype=torch.float32).unsqueeze(-1)
X_test = torch.tensor(X_test, dtype=torch.float32).unsqueeze(-1)
y_test = torch.tensor(y_test, dtype=torch.float32).unsqueeze(-1)

# Create DataLoader
train_dataset = TensorDataset(X_train, y_train)
test_dataset = TensorDataset(X_test, y_test)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

# Define GRU model
class GRUModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(GRUModel, self).__init__()
        self.gru = nn.GRU(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.gru(x)
        out = self.fc(out[:, -1, :])
        return out

# Define LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])
        return out

# Train function
def train_model(model, train_loader, criterion, optimizer, epochs=50):
    model.train()
    for epoch in range(epochs):
        for X_batch, y_batch in train_loader:
            optimizer.zero_grad()
            y_pred = model(X_batch)
            loss = criterion(y_pred, y_batch)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item()}")

# Evaluate function
def evaluate_model(model, test_loader):
    model.eval()
    predictions, actuals = [], []
    with torch.no_grad():
        for X_batch, y_batch in test_loader:
            y_pred = model(X_batch)
            predictions.extend(y_pred.numpy())
            actuals.extend(y_batch.numpy())
    return np.array(predictions), np.array(actuals)

# Train and evaluate GRU
gru_model = GRUModel(input_size=1, hidden_size=50, output_size=1)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(gru_model.parameters(), lr=0.01)
train_model(gru_model, train_loader, criterion, optimizer)
gru_predictions, _ = evaluate_model(gru_model, test_loader)

# Train and evaluate LSTM
lstm_model = LSTMModel(input_size=1, hidden_size=50, output_size=1)
optimizer = torch.optim.Adam(lstm_model.parameters(), lr=0.01)
train_model(lstm_model, train_loader, criterion, optimizer)
lstm_predictions, _ = evaluate_model(lstm_model, test_loader)

# ARIMA predictions
arima_predictions = arima_predict(train, test)

# Inverse transform predictions
gru_predictions = scaler_y.inverse_transform(gru_predictions.reshape(-1, 1)).flatten()
lstm_predictions = scaler_y.inverse_transform(lstm_predictions.reshape(-1, 1)).flatten()
arima_predictions = arima_predictions  # ARIMA predictions are already in the original scale

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(test, label="Actual Arriving Rate", color="black")
plt.plot(arima_predictions, label="ARIMA Predictions", linestyle="--")
plt.plot(gru_predictions, label="GRU Predictions", linestyle="-.")
plt.plot(lstm_predictions, label="LSTM Predictions", linestyle=":")
plt.xlabel("Time")
plt.ylabel("Arriving Rate")
plt.title("Comparison of ARIMA, GRU, and LSTM Predictions")
plt.legend()
plt.grid()
plt.show()