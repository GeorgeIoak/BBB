import smbus
bus = smbus.SMBus(1)

# device address, register address, [# of bytes, data1, data2, ...]
bus.write_i2c_block_data(0x2c, 0x00, [0x20, \
0x24, 0x04, 0x14, 0x25, 0xB3, 0x0B, 0x9B, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x32, 0x01, 0x32])

bus.write_i2c_block_data(0x2c, 0x10, [0x20, \
0x32, 0x04, 0x09, 0x13, 0x15, 0x0A, 0x49, 0x00, 0x4F, 0x00, 0x00, 0x00, 0x54, 0x00, 0x45, 0x00])

bus.write_i2c_block_data(0x2c, 0x20, [0x20, \
0x43, 0x00, 0x48, 0x00, 0x4E, 0x00, 0x4F, 0x00, 0x4C, 0x00, 0x4F, 0x00, 0x47, 0x00, 0x49, 0x00])

bus.write_i2c_block_data(0x2c, 0x30, [0x20, \
0x45, 0x00, 0x53, 0x00, 0x00, 0x00, 0x4C, 0x00, 0x4C, 0x00, 0x43, 0x00, 0x00, 0x00, 0x00, 0x00])

bus.write_i2c_block_data(0x2c, 0x40, [0x20, \
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

bus.write_i2c_block_data(0x2c, 0x50, [0x20, \
0x00, 0x00, 0x00, 0x00, 0x42, 0x00, 0x69, 0x00, 0x67, 0x00, 0x00, 0x00, 0x42, 0x00, 0x72, 0x00])

bus.write_i2c_block_data(0x2c, 0x60, [0x20, \
0x6F, 0x00, 0x74, 0x00, 0x68, 0x00, 0x65, 0x00, 0x72, 0x00, 0x00, 0x00, 0x42, 0x00, 0x61, 0x00])

bus.write_i2c_block_data(0x2c, 0x70, [0x20, \
0x73, 0x00, 0x65, 0x00, 0x62, 0x00, 0x6F, 0x00, 0x61, 0x00, 0x72, 0x00, 0x64, 0x00, 0x00, 0x00])

bus.write_i2c_block_data(0x2c, 0x80, [0x20, \
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

bus.write_i2c_block_data(0x2c, 0x90, [0x20, \
0x00, 0x00, 0x32, 0x00, 0x30, 0x00, 0x31, 0x00, 0x34, 0x00, 0x30, 0x00, 0x38, 0x00, 0x30, 0x00])

bus.write_i2c_block_data(0x2c, 0xA0, [0x20, \
0x30, 0x00, 0x30, 0x00, 0x31, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

#Battery Charging Enable
bus.write_i2c_block_data(0x2c, 0xD0, [0x01, 0xE1])

#Issue a USB Attach - Needed for the hub to enumerate
bus.write_i2c_block_data(0x2c, 0xFF, [0x01, 0x01])

#print bus.read_i2c_block_data(0x2c, 0x00)
#print bus.read_i2c_block_data(0x2c, 0x20)
#print bus.read_i2c_block_data(0x2c, 0x40)
#print bus.read_i2c_block_data(0x2c, 0x60)
#print bus.read_i2c_block_data(0x2c, 0x80)
#print bus.read_i2c_block_data(0x2c, 0xA0)
#print bus.read_i2c_block_data(0x2c, 0xC0)