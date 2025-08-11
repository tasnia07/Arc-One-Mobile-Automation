# Excel-Technologies-SQA-Assignment

## ABC Company Mobile App – Appium Automation Tests
Automated test scripts for the ABC Company Mobile App using Python + Appium on a real Android device.  
This project covers key test scenarios, including navigation, form submissions, and validation checks.

---

## i. Setup Instructions

### **Prerequisites**
- **Operating System**: Windows / macOS / Linux  
- **Real Android Device** with USB Debugging enabled  
- **USB Cable** to connect your device  
- **Appium Server** (Desktop or CLI) installed and running  
- **Android SDK & Platform Tools** installed (**adb** accessible from terminal)  
- **Python 3.7+** installed  

### **Enable USB Debugging**
On your Android device:
1. Go to **Settings → About Phone**
2. Tap **Build Number** 7 times to enable Developer Mode
3. Navigate to **Settings → Developer Options**
4. Enable **USB Debugging**

### **Verify Device Connection**
```bash
adb devices
```
You should see:

```bash
List of devices attached
fb82c273    device
```
If your device does not appear:

Check your USB cable & connection

Authorise USB debugging on your phone when prompted

## ii. Dependencies
Install the required Python packages:
```bash
pip install Appium-Python-Client selenium
```
iii. How to Run the Tests
Connect your device via USB and ensure it is recognised by ADB.

Start Appium Server (Desktop or CLI):
```bash
appium
```
Run the Python script:
```bash
python your_test_script.py
```
## iv. Screen Recording
All automation tests were executed on a real Android device.
The recording demonstrates every step executed by the script https://drive.google.com/drive/folders/1jXzOcfUfjoj1XQx0gNHQ1DbiNfT7a_vK?usp=drive_link

## v. Additional Notes
Adjust desired capabilities in the script for your device/app version

Keep your device unlocked during execution

If encountering permission errors, verify app permissions manually

For live observation of automation, use tools like scrcpy
