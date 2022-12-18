#include <stdio.h>

/*
	ons min hours
	ons max hours
	ons rate card
	off min hours
	off max hours
	off rate card
	target amount
*/

int main() {
	float ons_min_hours;
	float ons_max_hours;
	float ons_rate_card;
	float off_min_hours;
	float off_max_hours;
	float off_rate_card;
	float target_amount;

	float minmum_amount;
	float maxmum_amount;

	float ons_hours;
	float off_hours;
	float curr_amount;
	float ons_hours_loop;
	float off_hours_loop;
	char ons_hours_str[16];
	char off_hours_str[16];

/*
	ons_min_hours = 100.00;
	ons_max_hours = 160.00;
	ons_rate_card = 79.50;
	off_min_hours = 250.00;
	off_max_hours = 800.00;
	off_rate_card = 32.50;
	target_amount = 20000.00;
*/

	printf("ONS min hours: ");
	scanf("%f", &ons_min_hours);
	printf("ONS max hours: ");
	scanf("%f", &ons_max_hours);
	printf("ONS rate card: ");
	scanf("%f", &ons_rate_card);
	printf("OFF min hours: ");
	scanf("%f", &off_min_hours);
	printf("OFF max hours: ");
	scanf("%f", &off_max_hours);
	printf("OFF rate card: ");
	scanf("%f", &off_rate_card);
	printf("Target Amount: ");
	scanf("%f", &target_amount);

	printf("\nONS min hours: %f", ons_min_hours);
	printf("\nONS max hours: %f", ons_max_hours);
	printf("\nONS rate card: %f", ons_rate_card);
	printf("\nOFF min hours: %f", off_min_hours);
	printf("\nOFF max hours: %f", off_max_hours);
	printf("\nOFF rate card: %f", off_rate_card);
	printf("\nTarget Amount: %f", target_amount);


	printf("\n");
	minmum_amount = ons_min_hours*ons_rate_card + off_min_hours*off_rate_card;
	maxmum_amount = ons_max_hours*ons_rate_card + off_max_hours*off_rate_card;
	printf("\nPossible [Min, Max] = [%f, %f]\n", minmum_amount, maxmum_amount);
	if ((target_amount < minmum_amount) || (target_amount > maxmum_amount)) {
		printf("\nTarget amount is out of range. Tune the parameters and try again !\n\n");
		return 0;

	}

	for (ons_hours_loop = ons_max_hours; ons_hours_loop >= ons_min_hours; ons_hours_loop -= 0.01) {
		for (off_hours_loop = off_min_hours; off_hours_loop <= off_max_hours; off_hours_loop += 0.01) {
			sprintf(ons_hours_str, "%.2f", ons_hours_loop);
			sprintf(off_hours_str, "%.2f", off_hours_loop);
			sscanf(ons_hours_str, "%f", &ons_hours);
			sscanf(off_hours_str, "%f", &off_hours);
			curr_amount = (ons_hours * ons_rate_card) + (off_hours * off_rate_card);
			if (curr_amount == target_amount) {
				printf("\nons_hours_str = %s\t\toff_hours_str = %s", ons_hours_str, off_hours_str);
				// printf("\nons_hours = %f\t\toff_hours = %f\t\tcurr_amount = %f\t\ttarget_amount = %f", ons_hours, off_hours, curr_amount, target_amount);
			}
		}
	}
	printf("\n\n");
	return 0;
}
