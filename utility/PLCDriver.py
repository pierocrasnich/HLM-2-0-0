from pycomm3 import CIPDriver, CommonService

drive_path = '192.168.1.128'

with CIPDriver(drive_path) as drive:
    if drive.connected:
        data = drive.generic_message(
            service=CommonService.get_attribute_single,
            class_code=b'\x04',
            instance=198,
            attribute=3,
            connected=False,
            #unconnected_send=True,
            route_path=True,
            #data_format=[('Value', ''), ],
            name='Vendor'
        )
        print(str(data.value))
    else:
        print('Not Connected')