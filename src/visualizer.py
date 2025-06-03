import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib
import pandas as pd


def plot_trade_signals(df, stock_name="Stock"):
    plt.figure(figsize=(14, 6))

    # Use proper datetime index or column as x-axis
    x = df.index if isinstance(df.index, pd.DatetimeIndex) else df["date"]

    # Plot Adj Close vs Date
    plt.plot(x, df["Adj Close"], label="Adj Close", color="blue")

    # Buy markers
    buys = df[df["Buy_Signal"]]
    plt.scatter(buys.index if isinstance(df.index, pd.DatetimeIndex) else buys["date"],
                buys["Adj Close"], label="Buy", marker="^", color="green", s=100)

    # Sell markers
    sells = df[df["Sell_Signal"]]
    plt.scatter(sells.index if isinstance(df.index, pd.DatetimeIndex) else sells["date"],
                sells["Adj Close"], label="Sell", marker="v", color="red", s=100)

    plt.title(f"{stock_name} - Buy/Sell Signals")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)

    # Format x-axis to show only the year
    ax = plt.gca()  # get current axis
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.xticks(rotation=45)  # rotate if needed for better readability

    plt.show()



def plot_indicators(df, stock_name):
    try:
        plt.figure(figsize=(14, 8))

        plt.subplot(3, 1, 1)
        plt.plot(df["Adj Close"], label="Adj Close")
        plt.plot(df["MA20"], label="MA20")
        plt.title(f"{stock_name}: Adj Close & MA20")
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(df["RSI"], label="RSI", color="purple")
        plt.axhline(70, color='red', linestyle='--')
        plt.axhline(30, color='green', linestyle='--')
        plt.title("RSI")

        plt.subplot(3, 1, 3)
        plt.plot(df["MACD"], label="MACD")
        plt.plot(df["MACD_Signal"], label="MACD Signal")
        plt.title("MACD")
        plt.legend()

        plt.tight_layout()

        
        if matplotlib.get_backend() != "agg":
            plt.show()

    except Exception as e:
        print(f"Plotting failed for {stock_name}: {e}")
        
