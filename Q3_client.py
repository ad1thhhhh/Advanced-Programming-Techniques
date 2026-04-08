import socket
import json

HOST = '127.0.0.1'
PORT = 5000

def get_input():
    print("=== EasyDrive Registration ===")
    name = input("Enter your Name: ").strip()
    address = input("Enter your EIR Code: ").strip()
    pps = input("Enter your PPS Number: ").strip()
    license_doc = input("Enter your Driving License Number: ").strip()

    return {
        "name": name,
        "address": address,
        "ppsn": ppsn,
        "license": license_num
    }

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
        data = get_input()
        client.send(json.dumps(data).encode())

        response = client.recv(4096).decode()
        response = json.loads(response)

        if response["status"] == "success":
            print("\n✅ Registration Successful!")
            print("Registration Number:", response["reg_number"])
        else:
            print("\n❌ Error:", response["message"])

    except Exception as e:
        print("Connection error:", e)
    finally:
        client.close()

if __name__ == "__main__":
    main()
