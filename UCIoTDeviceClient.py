'''
 Copyright Urbanova 2019 | Licensed under the Apache License, Version 2.0 (the "License")
 This file is distributed on an "AS IS" BASIS,WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
 either express or implied. See the License for the specific language governing permissions
 and limitations under the License.
'''

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time

# Urbanova Cloud IoT Endpoint
UC_IOT_ENDPOINT = "a1siobcc26zf4j-ats.iot.us-west-2.amazonaws.com"

class UrbanovaCloudIoTClient():

  def __init__(self, deviceId, credentialsPath=""): # Todo: pass custom callback to handle subscription events

    self.deviceId = deviceId
    rootCAPath = credentialsPath + "rootCA.crt"
    privateKeyPath = credentialsPath + "thing.cert.pem"
    certificatePath =credentialsPath + "thing.private.key"

    # Init Urbanova Cloud IoT MQTT Client using TLSv1.2 Mutual Authentication
    self.mqttClient = None  # initialize var
    self.mqttClient = AWSIoTMQTTClient(self.deviceId) # The client class that connects to and accesses AWS IoT over MQTT v3.1/3.1.1.
    self.mqttClient.configureEndpoint(UC_IOT_ENDPOINT, 8883) # MQTT Broker host address and default port (TLS)
    self.mqttClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath) # certs and key

    # Configure Default MQTT Client Connection Settings (reference: https://s3.amazonaws.com/aws-iot-device-sdk-python-docs/sphinx/html/index.html)
    self.mqttClient.configureAutoReconnectBackoffTime(1, 32, 20)
    self.mqttClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    self.mqttClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    self.mqttClient.configureConnectDisconnectTimeout(10)  # 10 sec
    self.mqttClient.configureMQTTOperationTimeout(5)  # 5 sec

  # Connect to Urbanova Cloud
  def connect(self):
    self.mqttClient.connect()
    time.sleep(2)

  # Publish to Urbanova Cloud
  def publish(self, messageJson, qos=1):
    self.mqttClient.publish(self.deviceId, messageJson, qos) # publish to urbanova cloud