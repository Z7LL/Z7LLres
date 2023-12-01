## Z7LLres
Z7LLres is a tool for Windows to save custom settings in Fortnite.

![alphares](https://raw.githubusercontent.com/Z7LL/Z7LLres/master/Z7LLres/asset/Z7LLres.png)

## Download
* Go to [Releases](https://github.com/Z7LL/Z7LLres/releases/tag/V2.3.0)
* Under **Assets**, click "Z7LLres.exe"
* Move it to an accessible location (i.e., Documents, Desktop, etc.)

## Suspicious File or Virus
* You can view the virus scan from VirusTotal for the [Z7LLres](https://www.virustotal.com/gui/file/78fba4b227f52de6c9243bd65ddc7aa126f0e780a6a34964f1ff0e0b1f6e22ff/detection) release.
* Chrome or Firefox might detect it as suspicious, because I have released a new version. However, as more people download it, then the warning should disappear. You should still be able to download the file.
* Windows Defender will flag software without a certificate or from unknown sources, so there are often false positives. The solution to this is to purchase a certificate from a Certificate Authority, but this can be expensive for a small developer. Read more [here](https://stackoverflow.com/questions/252226/signing-a-windows-exe-file). As a workaround, I can "self-sign" the software, however, this will lead to Windows SmartScreen warning you about running the file.
* Windows SmartScreen will state that: "Microsoft Defender SmartScreen prevented an unrecognized app from starting. Running this app might put your PC at risk". However, if you press "More Info", then you will be able to run the program by pressing "Run anyway". I hope as more people download it, then the program will become more trusted and Microsoft will no longer flag it.
* If you are using another anti-virus and alphares is detected as a virus, then you can add alphares as an exception. I do not have time to contact each anti-virus vendor, and ask them to allow it.
* **If you do not feel safe, then please do not download Z7LLres. Alternatively, if you have experience in software, then you can review the code or compile it yourself by running:** `auto-py-to-exe or pyinstaller`.

## How to use
* Open the "Z7LLres" executable
* Change the `Width` and `Height` to a desired resolution
* Click on "Read-only" so the box is checked
* Press "Apply"
* You *might* also have to change the settings in the NVIDIA or AMD Control Panel

## Uninstall

There is nothing to uninstall.

If you want to delete Z7LLres, then just delete or move `Z7LLres.exe` to the Recycle Bin.

If you want to "undo" the changes made from using Z7LLres, then you must:

1. Close Fortnite.
2. Press `Win + R` to open a "Run" window.
3. In the box, type: `%localappdata%` and press Enter.
4. From there, you will have to navigate to: `FortniteGame/Saved/Config/WindowsClient/GameUserSettings.ini`.
5. Right-click on `GameUserSettings.ini`, then select "Properties".
6. A dialog box will open where you can uncheck the "Read-only" box, and then press "Apply".
7. Open Fortnite.

This should allow Fortnite to overwrite the settings that were saved from alphares. However, if that does not work, then you will have to delete the `GameUserSettings.ini` file. Please keep in mind that this will reset all settings.

1. Close Fortnite.
2. Press `Win + R` to open a "Run" window.
3. In the box, type: `%localappdata%` and press Enter.
4. From there, you will have to navigate to: `FortniteGame/Saved/Config/WindowsClient/GameUserSettings.ini`.
5. Delete `GameUserSettings.ini`.
6. Open Fortnite.

## Popular resolution(s)
* 1600x1080
* 1440x1080
* 1280x1024
* 1154x1080
* 1080x1080

## Support
If you want to support what I do, consider making a donation:
* [PayPal](https://www.paypal.com/myaccount/transfer/homepage/buy/preview)

## Note
* You must have launched Fortnite at least once, and allowed the game to detect the best settings or saved custom settings in-game before running Z7LLres.
* Z7LLres can set/unset the configuration file's read-only attribute. This is to prevent Fortnite from updating the configuration file and resetting the custom resolution. As such, you will be unable to save settings in-game while it is set. You must uncheck the read-only box and press "Apply" to save changes.
* If you want to have an uncapped framerate in Fortnite, you must set the FPS field to `0` in Z7LLres.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
