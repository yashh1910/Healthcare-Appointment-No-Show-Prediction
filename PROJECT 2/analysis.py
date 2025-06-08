import pandas as pd

print("🔄 Loading dataset...")

try:
    # Load the dataset
    df = pd.read_csv('ecommerce_returns_synthetic_data.csv')
    print("✅ Dataset loaded successfully!")

    # Show first few rows
    print("\n👀 First 5 rows of data:")
    print(df.head())

    # Fill missing return status
    df['Return_Status'] = df['Return_Status'].fillna('Not Returned')

    # Create Is_Returned column
    df['Is_Returned'] = df['Return_Status'].apply(lambda x: 1 if x == 'Returned' else 0)

    # Fill missing return reason
    df['Return_Reason'] = df['Return_Reason'].fillna('No Return')

    # Convert dates
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    df['Return_Date'] = pd.to_datetime(df['Return_Date'])

    # Create Days_to_Return
    df['Days_to_Return'] = (df['Return_Date'] - df['Order_Date']).dt.days
    df['Days_to_Return'] = df['Days_to_Return'].fillna(0)

    # Save cleaned data
    df.to_csv('cleaned_ecommerce_data.csv', index=False)
    print("\n✅ Cleaned data saved as 'cleaned_ecommerce_data.csv'")

except FileNotFoundError:
    print("❌ File not found. Make sure 'ecommerce_returns_synthetic_data.csv' is in the same folder.")
except Exception as e:
    print("⚠️ Something went wrong:", e)
    input("Press Enter to exit...")

