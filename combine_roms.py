import os

def calculate_checksum(data):
    # Standard Sega Genesis checksum calculation
    # Sum of all 16-bit words starting from offset 0x200
    checksum = 0
    for i in range(0x200, len(data), 2):
        if i + 1 < len(data):
            checksum = (checksum + (data[i] << 8 | data[i+1])) & 0xFFFF
    return checksum

def combine_roms():
    s1_path = "Sonic The Hedgehog (USA, Europe).bin"
    s2_path = "Sonic The Hedgehog 2 (World).bin"
    s3k_path = "Sonic The Hedgehog 3 & Knuckles (World).bin"
    output_path = "Sonic Classic Trilogy - Ultimate Complete.bin"

    if not all(os.path.exists(p) for p in [s1_path, s2_path, s3k_path]):
        print("Error: One or more base ROMs are missing.")
        return

    print("Reading Sonic 1...")
    with open(s1_path, "rb") as f:
        s1_data = f.read()
    
    print("Reading Sonic 2...")
    with open(s2_path, "rb") as f:
        s2_data = f.read()

    print("Reading Sonic 3 & Knuckles...")
    with open(s3k_path, "rb") as f:
        s3k_data = f.read()

    # Concatenate ROMs
    combined_data = bytearray(s1_data + s2_data + s3k_data)
    
    # Update Header
    print("Updating Header at 0x100 to SEGA SSF...")
    combined_data[0x100:0x110] = b"SEGA SSF        "
    
    print("Updating ROM End Address at 0x1A4 to 0x0057FFFF...")
    combined_data[0x1A4:0x1A8] = bytes.fromhex("0057FFFF")
    
    # Calculate and Update Checksum
    print("Calculating Checksum...")
    checksum = calculate_checksum(combined_data)
    print(f"Checksum calculated: {hex(checksum)}")
    combined_data[0x18E:0x190] = checksum.to_bytes(2, byteorder='big')

    # Save output
    print(f"Saving to {output_path}...")
    with open(output_path, "wb") as f:
        f.write(combined_data)
    
    print("Combined ROM successfully created!")

if __name__ == "__main__":
    combine_roms()
