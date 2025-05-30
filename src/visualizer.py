import matplotlib.pyplot as plt
import matplotlib

def plot_trade_signals(df, stock_name="Stock"):
       #Plot Adj Close with Buy (green arrow) and Sell (red arrow) signals.
    
    plt.figure(figsize=(14, 6))
    plt.plot(df["Adj Close"], label="Adj Close", color="blue")

    # Buy markers
    buys = df[df["Buy_Signal"]]
    plt.scatter(buys.index, buys["Adj Close"], label="Buy", marker="^", color="green", s=100)

        # Sell markers
    sells = df[df["Sell_Signal"]]
    plt.scatter(sells.index, sells["Adj Close"], label="Sell", marker="v", color="red", s=100)

    plt.title(f"{stock_name} - Buy/Sell Signals")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    
    if matplotlib.get_backend() != "agg":
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
        
