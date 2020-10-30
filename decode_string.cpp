#include <iostream>
#include <cstdint>
#include <cstring>

int32_t PPPP_DecodeString(const char* input, char* output, size_t length);

/**
 * Decodes an initializer string.  The input string contains the characters A-P (base-16).
 * The expected output is a number of comma-separated IP addresses.
 * 
 * @return 0 on success, -1 if output buffer length is greater than double input length
 */
int32_t PPPP_DecodeString(const char* input, char* output, size_t length) {
	// this is a lookup table in libPPPP_API.so
	// the values are the same in com.hbwy.fan.iminicams and com.p2pcamera.app01
	static uint8_t lut[0x36];
	static_assert(sizeof(lut) == 0x36, "PPPP_DecodeString::lut size mismatch");
	
	size_t inputlen = strlen(input);
	for (size_t i = 0; i < length; i++) {
		if (inputlen / 2 <= i) {
			return 0;
		}
		uint8_t bVar7 = 0x39;
		for (size_t j = 0; j < i; j++) {
			bVar7 = bVar7 ^ output[j];
		}
		// output = (some_xor_operation ^ second_char_as_hex + (first_char_as_hex << 4)
		output[i] = bVar7 ^ lut[i % 0x36] ^ (input[i * 2 + 1] - 'A') + (input[i * 2] - 'A') * '\x10';
	}
	return -1; // disassembly actually returns 0xffffffff
}
