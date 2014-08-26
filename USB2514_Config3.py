import smbus
bus = smbus.SMBus(1)

# device address, register address, [# of bytes, data1, data2, ...]

regvals=[
[0x10, 0x24, 0x04, 0x14, 0x25, 0xB3, 0x0B, 0x9B, 0x30, 0x00, 0x00, 0x00, 0x00, 0x01, 0x32, 0x01, 0x32], # 0x00
[0x10, 0x32, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], # 0x10
[0x10, 0x43, 0x00, 0x48, 0x00, 0x4E, 0x00, 0x4F, 0x00, 0x4C, 0x00, 0x4F, 0x00, 0x47, 0x00, 0x49, 0x00], # 0x20
[0x10, 0x45, 0x00, 0x53, 0x00, 0x00, 0x00, 0x4C, 0x00, 0x4C, 0x00, 0x43, 0x00, 0x00, 0x00, 0x00, 0x00], # 0x30
[0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], # 0x40
[0x10, 0x00, 0x00, 0x00, 0x00, 0x42, 0x00, 0x69, 0x00, 0x67, 0x00, 0x00, 0x00, 0x42, 0x00, 0x72, 0x00], # 0x50
[0x10, 0x6F, 0x00, 0x74, 0x00, 0x68, 0x00, 0x65, 0x00, 0x72, 0x00, 0x00, 0x00, 0x42, 0x00, 0x61, 0x00], # 0x60
[0x10, 0x73, 0x00, 0x65, 0x00, 0x62, 0x00, 0x6F, 0x00, 0x61, 0x00, 0x72, 0x00, 0x64, 0x00, 0x00, 0x00], # 0x70
[0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], # 0x80
[0x10, 0x00, 0x00, 0x32, 0x00, 0x30, 0x00, 0x31, 0x00, 0x34, 0x00, 0x30, 0x00, 0x38, 0x00, 0x30, 0x00], # 0x90
[0x10, 0x30, 0x00, 0x30, 0x00, 0x31, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]]  # 0xA0

y = 0
for x in range(0, 32, 16):
#	regvals.insert(0, 0x20)
#	print x, y, regvals[y]
	bus.write_i2c_block_data(0x2c, x, regvals[y])
	y = y + 1


#Battery Charging Enable, reverse byte order?
bus.write_i2c_block_data(0x2c, 0xD0, [0x01, 0x1E])

#Need to swap D+/D- line on Downstream Ports
bus.write_i2c_block_data(0x2c, 0xFA, [0x01, 0x1E])


#Issue a USB Attach - Needed for the hub to enumerate
bus.write_i2c_block_data(0x2c, 0xFF, [0x01, 0x01])
#bus.write_i2c_block_data(0x2c, 0xFF, [0x01, 0x00])
