import qrcode

print("\n" + "="*40)
print("   📱 QR CODE GENERATOR")
print("="*40)

text = input("\n🔗 Enter text or URL: ")

qr = qrcode.make(text)
qr.save("my_qrcode.png")

print("\n✅ QR Code saved as 'my_qrcode.png'")
print("📂 Check your folder for the image!\n")