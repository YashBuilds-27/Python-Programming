import qrcode as qr
# -------------------- INPUT FUNCTION --------------------
def take_input(msg):
    data = input(f"{msg}: ").strip()
    filename = input("Enter filename to save QR (eg: qrcode.png): ").strip()
    if filename == "":
        filename = "qrcode"
    if not filename.endswith(".png"):
        filename += ".png"
    return data, filename

# -------------------- QR GENERATOR --------------------
def generate_qr(data, filename):
    try:
        img = qr.make(data)
        img.save(filename)
        print(f"\n✅ QR Code saved as {filename}")
    except Exception:
        print("❌  An Unknown Error occurred:")

# -------------------- PAYMENT QR --------------------
def payment_qr():
    upi = input("Enter UPI ID (eg: user@upi): ").strip()
    name = input("Enter Name (eg: John Doe): ").strip()
    amount = input("Enter Amount (eg: 100): ").strip()
    filename = input("Enter filename (eg: payment_qr.png): ").strip()
    if filename == "":
        filename = "payment_qr"
    if not filename.endswith(".png"):
        filename += ".png"
    data = f"upi://pay?pa={upi}&pn={name}&am={amount}"
    generate_qr(data, filename)

# -------------------- MENU --------------------
def menu():
    while True:
        print("""
========== QR CODE GENERATOR ==========
1. Generate QR Code
2. Exit
======================================
""")
        choice = input("Enter choice (1-2): ").strip()
        if choice == "1":
            while True:
                print("""
1. Text QR Code
2. URL QR Code
3. Payment QR Code
4. Back
""")
                choice2 = input("Enter choice (1-4): ").strip()
                if choice2 == "1":
                    data, filename = take_input("Enter text")
                    generate_qr(data, filename)
                elif choice2 == "2":
                    data, filename = take_input("Enter URL (eg: https://example.com)")
                    generate_qr(data, filename)
                elif choice2 == "3":
                    payment_qr()
                elif choice2 == "4":
                    break
                else:
                    print("❌ Invalid Choice Try Again")
        elif choice == "2":
            print("\nThank you for using QR Generator👋")
            break
        else:
            print("❌ Invalid Choice Try Again")

# -------------------- START --------------------
menu()
