# hex to float32 부동소수점 변환
import struct
print(struct.unpack('!f', bytes.fromhex('41233333'))[0])
