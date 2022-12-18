#include <stdio.h>
#include <string.h>

#define E31_DIGITS_COUNT 31

// kept as char array instead of string for better visualisation
char e31_digits[] = {
	'2', '3', '4', '5', '6',
	'7', '8', '9', 'A', 'B',
	'C', 'D', 'E', 'F', 'G',
	'H', 'J', 'K', 'M', 'N',
	'P', 'Q', 'R', 'S', 'T',
	'U', 'V', 'W', 'X', 'Y',
	'Z'
};


/*
 * Return value:
 *      0: Invalid E31 digit 
 *      1: Valid E31 digit 
 */
int valid_e31_digit (char c) {
	switch (c) {
		case '2' :
		case '3' :
		case '4' :
		case '5' :
		case '6' :
		case '7' :
		case '8' :
		case '9' :
		case 'A' :
		case 'B' :
		case 'C' :
		case 'D' :
		case 'E' :
		case 'F' :
		case 'G' :
		case 'H' :
		case 'J' :
		case 'K' :
		case 'M' :
		case 'N' :
		case 'P' :
		case 'Q' :
		case 'R' :
		case 'S' :
		case 'T' :
		case 'U' :
		case 'V' :
		case 'W' :
		case 'X' :
		case 'Y' :
		case 'Z' :
			return (1);
		default:
			return (0);
	}
	return (0);
}

int e31_to_int (char c) {
	switch (c) {
		case '2' :
			return (0);
		case '3' :
			return (1);
		case '4' :
			return (2);
		case '5' :
			return (3);
		case '6' :
			return (4);
		case '7' :
			return (5);
		case '8' :
			return (6);
		case '9' :
			return (7);
		case 'A' :
			return (8);
		case 'B' :
			return (9);
		case 'C' :
			return (10);
		case 'D' :
			return (11);
		case 'E' :
			return (12);
		case 'F' :
			return (13);
		case 'G' :
			return (14);
		case 'H' :
			return (15);
		case 'J' :
			return (16);
		case 'K' :
			return (17);
		case 'M' :
			return (18);
		case 'N' :
			return (19);
		case 'P' :
			return (20);
		case 'Q' :
			return (21);
		case 'R' :
			return (22);
		case 'S' :
			return (23);
		case 'T' :
			return (24);
		case 'U' :
			return (25);
		case 'V' :
			return (26);
		case 'W' :
			return (27);
		case 'X' :
			return (28);
		case 'Y' :
			return (29);
		case 'Z' :
			return (30);
		default:
			return (-1);
	}
	return (-1);
}

void strrev( char *str) {
	int i, len;
	char c;

	len = strlen(str);
	if (len <= 1) {
		return;
	}

	i = len / 2;
	while (i) {
		i--;
		c = str[i];
		str[i] = str[(len - 1) - i];
		str[(len - 1) - i] = c;
	}
}

/*
 * Notes:
 *
 * width - to pad extra E31 zeros ('2') to the derived E31 encoded string so that the
 *         final length matches width. width = 0 means no padding required.
 * 
 * Return value:
 *		0: Success case 
 *		1: NULL output string 
 *		2: Width not sufficient
 */
int e31_encode (unsigned long int decimal_input, unsigned int width, char *e31_output) {
	int actual_e31_digits, i;

	if (NULL == e31_output) {
		return (1);
	}

	actual_e31_digits = 0;
	do {
		e31_output[actual_e31_digits] = e31_digits[decimal_input % E31_DIGITS_COUNT];
		decimal_input /= E31_DIGITS_COUNT;
		actual_e31_digits++;
	} while (decimal_input > 0);

	// Prefix with extra is to add missing digits 
	if (width != 0) {
		 if (actual_e31_digits > width) {
			e31_output[0] = '\0'; // reset the string to NULL
			return (2);
		}

		i = width - actual_e31_digits; // number of paddings required.
		e31_output[width] = '\0';
		while (i) {
			e31_output[actual_e31_digits + i - 1] = e31_digits[0];
			i--;
		}
	} else {
		e31_output[actual_e31_digits] = '\0';
	}

	strrev(e31_output);
	return (0);
}

/*
 * Return value:
 * 		0: Decimal value derived successfully
 * 		1: NULL output string 
 * 		2: Empty string 
 * 		3: Invalid E31 digits 
 * 		4: E31 digit to decimal conversion error  
 */
int e31_decode (char *e31_input, unsigned long int *decimal_value, unsigned int *width) {
	unsigned long int pow_31, int_val;
	int  len, i;

	if (NULL == e31_input) {
		return (1);
	}

	len = strlen(e31_input);
	if (len <= 0) {
		return (2);
	}

	*width = 0;
	if ((len > 1) && (e31_input[0] == e31_digits[0])) {
		//Width is applicable only for E31 value that has more than one digit.
		// If the first value in the inputs starts (padded) with E31 digit zero ('2'),  
		// then complete length of the E31 input is the width irrespective of any further
		// successive padding with E31 digit zero ('2').
		*width = len;
	}
	pow_31 = 1;
	*decimal_value = 0;
	strrev(e31_input);
	for (i = 0; i < len; i++) {
		if (!valid_e31_digit(e31_input[i])) {
			strrev(e31_input);
			return (3);
		}
		int_val = e31_to_int(e31_input[i]);
		if (int_val < 0) {
			strrev(e31_input);
			return (4);
		}
		*decimal_value += pow_31*int_val;
		pow_31 *= E31_DIGITS_COUNT;		
	}
	strrev(e31_input);
	return (0);
}

int main (void) {
	char opt;
	unsigned long int num;
	unsigned int width;
	int ret, offset;
	char e31_enc_value[32] = {0};
	char e31_dec_value[32] = {0};
	int  enc_error_count = 3;
	char *enc_ret_str[] = {
		"Success case",
		"NULL output string",
		"Width not sufficient",
	}; 
	int  dec_error_count = 5;
	char *dec_ret_str[] = {
		"Decimal value derived successfully",
		"NULL output string",
		"Empty string",
		"Invalid E31 digits",
		"E31 digit to decimal conversion error"
	};

	num = ~0;
	printf("\nMax possible decimal number using unsigned long     : %lu\n", num);
	printf("List of digits used for E31 encoding                : %s\n", e31_digits);
	e31_encode(num, 0, e31_enc_value);
	printf("Max possible E31 encoded number using unsigned long : %s\n", e31_enc_value);

	do {
		printf("\nOperations symbol: encode(e) / decode(d) / add(a) / subtract(s) / exit(x)\n");
		printf("Enter the operation symbol: ");
		do {opt = getchar();} while ('\n' == opt);

		switch (opt) {
		case 'e' :
			// Encoding section
			printf("\nEnter decimal number: ");
			scanf(" %ld", &num);
			printf("Enter the final width required (0 = default): ");
			scanf(" %d", &width);

			ret = e31_encode(num, width, e31_enc_value);
			printf("Encoding result: %d (%s)\n", ret, enc_ret_str[ret]);
			printf("Entered number: %lu\n", num);
			printf("Required width: %d\n", width);
			printf("E31 encoded number: %s\n", e31_enc_value);

			break;

		case 'd' :
			// Decoding section
			printf("\nEnter E31 number: ");
			scanf(" %s", e31_dec_value);

			ret = e31_decode(e31_dec_value, &num, &width);
			printf("Decoding result: %d (%s)\n", ret, dec_ret_str[ret]);
			printf("Entered E31 encoded number: %s\n", e31_dec_value);
			printf("Width detected (0 = default): %d\n", width);
			printf("Decoded decimal number: %lu\n\n", num);

			break;

		case 'a' :
			// Adding section
			printf("\nEnter E31 number: ");
			scanf(" %s", e31_dec_value);
			printf("Enter decimal offset to add: ");
			scanf(" %d", &offset);

			ret = e31_decode(e31_dec_value, &num, &width);
			printf("Decoding result: %d (%s)\n", ret, dec_ret_str[ret]);
			printf("Entered E31 encoded number: %s\n", e31_dec_value);
			printf("Width detected (0 = default): %d\n", width);
			printf("Decoded decimal number: %lu\n", num);
			printf("Offset decimal number to add: %d\n", offset);
			ret = e31_encode(num + offset, width, e31_enc_value);
			printf("Encoding result: %d (%s)\n", ret, enc_ret_str[ret]);
			printf("E31 encoded number: %s\n", e31_enc_value);

			break;

		case 's' :
			// Subtract section
			printf("\nEnter E31 number: ");
			scanf(" %s", e31_dec_value);
			printf("Enter decimal offset to subtract: ");
			scanf(" %d", &offset);

			ret = e31_decode(e31_dec_value, &num, &width);
			printf("Decoding result: %d (%s)\n", ret, dec_ret_str[ret]);
			printf("Entered E31 encoded number: %s\n", e31_dec_value);
			printf("Width detected (0 = default): %d\n", width);
			printf("Decoded decimal number: %lu\n", num);
			printf("Offset decimal number to subtract: %d\n", offset);
			ret = e31_encode(num - offset, width, e31_enc_value);
			printf("Encoding result: %d (%s)\n", ret, enc_ret_str[ret]);
			printf("E31 encoded number: %s\n", e31_enc_value);

			break;

		case 'x' :
			printf("\nExiting...\n\n");

			break;

		default:
			printf("Invalid operation '%c'. Retry with correct operation code.\n", opt);

			break;
		}		
	} while (opt != 'x');

	return (0);
}

