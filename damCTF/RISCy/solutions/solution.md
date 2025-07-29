## RISCy Business

Simple static rev challenge on an embedded RISCV device.

## Solve process

1. Identify architecture of elf (`file esp_ota_client.elf`) as 32-bit RISCV
2. Open up the `.elf` in a decompiler or use `strings`
3. Identify library imports, specifically the use of FreeRTOS
4. Look up FreeRTOS documentation for the name of the main fuction (`app_main()`)
5. Go to `app_main()` in a decompiler (Ghidra supports Xtensa/32-bit RSICV)
6. Follow function calls to find the call to `build_flag_task` function.
7. Inside `build_flag_task` determine how the flag string is built
   - The string is identifiable as it starts with `dam{`
   - There is a call to `strcat`, look up refrences to the `sharedString` variable to figure out what it would be set to
   - assemble all the chars in the flag string
8. Submit

## Commentary

If anyone managed to get this running in an emulator, congrats! The intention was to make this a static rev challenge as the emulator for this device is a bit annoying to get working (forked QEMU).