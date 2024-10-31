import os

try:
    for stream in open('..\\pswfeltrinelli.txt', 'r'):
        print(stream, end=' ')
    print()
except IOError as stream_ex:
    print(os.strerror(stream_ex.errno))

byte_array_in = bytearray(6774)
byte_array_out = bytearray(6774)

binary_stream_in = open('download.png', 'rb')
binary_stream_in.readinto(byte_array_in)

binary_stream_out = open('download - Copia.png', 'wb')
binary_stream_out.write(byte_array_in)





