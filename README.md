# urbanova-cloud-iot-sdk-python
Urbanova Cloud IoT SDK for Python

To use this SDK you will need an Urbanova Cloud Account (currently in Alpha).

#### Getting Started

* From your Urbanova Cloud account, add a new Data Source, select the Internet of Things / Urbanova IoT SDK option.

* From the IoT Data Source configuration options, choose Connection Kit, and click the 'Download Urbanova Cloud IoT Connection Kit for Linux/Python' link.

* The connection kit provides the deviceId and credentials (keys and certificates) required to securely connect your IoT edge device to Urbanova Cloud using the Urbanova IoT SDK.

The following example shows how to use the Urbanova IoT SDK for Python to connect and send messages to Urbanova Cloud:

```python
from UrbanovaCloudIoTSDK import UrbanovaCloudIoTClient
import json
import time

# Your Device ID from Urbanova Cloud IoT Connection Kit
deviceId = "25912a1f-08d5-4198-9f3d-2c14a3274b66" # use your device id

# Initialize Urbanova Cloud IoT Client Object
ucIoTClient = UrbanovaCloudIoTClient(deviceId, "path-to-credentials/")

# Publish Messages (one message per second)
loopCount = 0
while True:
  message = {} # init empty message obj
  message['message'] = 'Hello Sensor ' + deviceId # add `message` element
  message['sequence'] = loopCount # add `sequence` element
  messageJson = json.dumps(message) # convert to json
  ucIoTClient.publish(messageJson) # publish to urbanova cloud
  print('Published to %s: %s\n' % (deviceId, messageJson)) # print console
  loopCount += 1 # increment counter
  time.sleep(1) # delay one second
  ```
