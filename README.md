# Sonic Classic Trilogy - Ultimate Complete

**Created by Esrael Neto © 2026**

Welcome to the official repository and documentation for **Sonic Classic Trilogy - Ultimate Complete**. This project is a brand new Sega Genesis/Mega Drive ROM hack that combines the legendary classic titles—*Sonic the Hedgehog*, *Sonic the Hedgehog 2*, and *Sonic the Hedgehog 3 & Knuckles*—into a single, massive 5.5MB combined ROM file (`Sonic Classic Trilogy - Ultimate Complete.bin`). 

This comprehensive guide details the technical structure of the combined ROM, the methodology for merging the binaries, and how to utilize **Esrael Sonic Editor II** for further modifications and level editing.

---

## 1. Project Overview

The goal of this project is to provide a seamless, unified experience of the classic Sonic trilogy on original Sega Genesis hardware and emulators. By combining the individual game ROMs, we create a single binary that houses all three games.

### ROM Components and File Sizes
The combined ROM is exactly **5.5 MB (5,767,168 bytes)**, structured from the following original binaries:
| Game | Original Size | Offset Start | Offset End |
| :--- | :--- | :--- | :--- |
| **Sonic the Hedgehog** | 512 KB (0.5 MB) | `0x00000000` | `0x0007FFFF` |
| **Sonic the Hedgehog 2** | 1,024 KB (1.0 MB) | `0x00080000` | `0x0017FFFF` |
| **Sonic 3 & Knuckles** | 4,096 KB (4.0 MB) | `0x00180000` | `0x0057FFFF` |

---

## 2. Technical Details: Overcoming the 4MB Limit

The standard Sega Genesis memory map only allocates 4MB of address space for cartridge ROM data (from `0x000000` to `0x3FFFFF`). Because our combined ROM is 5.5MB, it exceeds this standard limitation [1].

To ensure the ROM functions correctly on emulators and flash cartridges, the ROM header must be modified to utilize the **Sega Mapper (SSF2 Mapper)**. Originally developed for *Super Street Fighter II*, this bank-switching mapper allows the console to access ROM sizes up to 32MB by swapping 512KB banks into the readable memory space [2].

### ROM Header Modifications
To instruct the emulator or hardware to use the SSF2 mapper, the console name field in the ROM header (located at offset `0x100`) must be changed to `SEGA SSF`. 

The updated header for the 5.5MB ROM is configured as follows:
*   **Console Name:** `SEGA SSF` (Enables bank-switching support)
*   **Copyright:** `(C)SEGA 2026.MAR`
*   **Domestic/Overseas Name:** `SONIC CLASSIC TRILOGY - ULTIMATE COMPLETE`
*   **ROM End Address:** `0x0057FFFF`
*   **Checksum:** Recalculated to validate the new 5.5MB binary structure.

---

## 3. How to Combine the ROMs

If you wish to build the combined ROM manually from your own legal backups, follow these technical steps. The process involves concatenating the binaries and updating the 68000 ROM header.

### Step-by-Step Concatenation
1.  **Extract the Binaries:** Ensure you have the clean, unheadered `.bin` files for Sonic 1, Sonic 2, and Sonic 3 & Knuckles.
2.  **Merge the Files:** Append the files in sequential order. Sonic 1 comes first, followed by Sonic 2, and finally Sonic 3 & Knuckles. 
    *   *Note: Because the sizes of Sonic 1 (512KB) and Sonic 2 (1MB) perfectly align with the 512KB bank boundaries of the SSF2 mapper, no additional padding bytes are required between the ROMs.*
3.  **Update the Header:** Open the merged binary in a Hex Editor.
    *   Navigate to offset `0x100` and change the system string to `SEGA SSF        `.
    *   Update the ROM End address at `0x1A4` to `00 57 FF FF`.
4.  **Fix the Checksum:** Use a Genesis checksum utility to recalculate the header checksum at offset `0x18E`.

A Python script is included in the development workflow of this repository to automate the concatenation and header injection process.

---

## 4. Using Esrael Sonic Editor II

**Esrael Sonic Editor II** (ESEII) is a powerful, multi-purpose modding tool created by Esrael Neto. It is widely recognized in the Sonic ROM hacking community for its comprehensive suite of features, including a level editor, art editor, palette editor, and built-in hex editor [3].

### Modifying the Combined ROM
While ESEII was originally designed to open individual ROMs (Sonic 1, Sonic 2, Sonic 3 & K), it can be utilized to modify the **Sonic Classic Trilogy - Ultimate Complete** ROM with specific configurations:

1.  **Bank Targeting:** Because the combined ROM uses bank-switching, you must ensure that ESEII is targeting the correct memory offsets when loading level data. 
    *   To edit Sonic 1 levels, target the `0x000000 - 0x07FFFF` range.
    *   To edit Sonic 2 levels, target the `0x080000 - 0x17FFFF` range.
    *   To edit Sonic 3 & Knuckles levels, target the `0x180000 - 0x57FFFF` range.
2.  **Level Editing:** Use ESEII's visual interface to modify object placements, ring layouts, and enemy spawn coordinates across all three games.
3.  **Palette Adjustments:** The built-in palette editor can be used to create unified color schemes or distinct atmospheric changes for the ultimate trilogy experience.
4.  **Saving Changes:** After making edits in ESEII, always recalculate the ROM checksum before testing the 5.5MB `.bin` file in an emulator like Kega Fusion or Genesis Plus GX.

---

## References

[1] Plutiedev. "ROM header reference." *Plutiedev*, https://plutiedev.com/rom-header.
[2] Sonic Retro. "Genesis OS Hacking Guide." *Sonic Retro Forums*, https://forums.sonicretro.org/threads/genesis-os-hacking-guide.14929/.
[3] Sonic Retro. "Esrael Sonic Editor II." *Sonic Retro Wiki*, https://info.sonicretro.org/Esrael_Sonic_Editor_II.
