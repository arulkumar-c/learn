#include <stdio.h>

#define X_ROWS  9
#define Y_COLS  9

int mine_filed[X_ROWS][Y_COLS] = {
{0, 1, 1, 1, 1, 0, 0, 1, 1},
{1, 1, 0, 0, 0, 0, 0, 1, 1},
{1, 1, 0, 0, 0, 0, 0, 1, 1},
{0, 0, 0, 0, 0, 0, 0, 1, 1},
{0, 0, 0, 0, 0, 0, 0, 0, 1},
{0, 0, 0, 0, 0, 0, 0, 0, 1},
{1, 1, 0, 0, 0, 0, 0, 0, 0},
{1, 0, 0, 0, 0, 0, 0, 0, 0},
{1, 1, 0, 0, 0, 0, 0, 0, 0}
};

int result_filed[X_ROWS][Y_COLS];

void fill_results (void) {
	int i, j;

	for (i = 0; i < X_ROWS; i++)
		for (j = 0; j < Y_COLS; j++)
			result_filed[i][j] = -1;
}

void print_matrix (int mat[][Y_COLS], int x, int y) {
	int i, j;

	printf("\n");
	for (i = 0; i < X_ROWS; i++) {
		for (j = 0; j < Y_COLS; j++)
			if ((i == x) && (j ==y))
				printf("(%d)  ", mat[i][j]);
			else
				printf("%2d   ", mat[i][j]);
		printf("\n");
	}
	printf("\n");

}

void count_mines (int x, int y) {
	int count_top, count_top_right, count_right, count_bottom_right, count_bottom, count_bottom_left, count_left, count_top_left;
	int top_exists, top_right_exists, right_exists, bottom_right_exists, bottom_exists, bottom_left_exists, left_exists, top_left_exists;

	if (result_filed[x][y] != -1)
		return;

	count_top = 0;
	count_top_right = 0;
	count_right = 0;
	count_bottom_right = 0;
	count_bottom = 0;
	count_bottom_left = 0;
	count_left = 0;
	count_top_left = 0;
	
	top_exists = 0;
	top_right_exists = 0;
	right_exists = 0;
	bottom_right_exists = 0;
	bottom_exists = 0;
	bottom_left_exists = 0;
	left_exists = 0;
	top_left_exists = 0;

	if (x > 0) {
		count_top = mine_filed[x - 1][y];
		top_exists = 1;
	}

	if ((x > 0) && (y < (Y_COLS - 1))) {
		count_top_right = mine_filed[x - 1][y + 1];
		top_right_exists = 1;
	}

	if (y < (Y_COLS - 1)) {
		count_right = mine_filed[x][y + 1];
		right_exists = 1;
	}
	
	if ((x < (X_ROWS - 1)) && (y < (Y_COLS - 1))) {
		count_bottom_right = mine_filed[x + 1][y + 1];
		bottom_right_exists = 1;
	}
	
	if (x < (X_ROWS - 1)) {
		count_bottom = mine_filed[x + 1][y];
		bottom_exists = 1;
	}
	
	if ((x < (X_ROWS - 1)) && (y > 0)) {
		count_bottom_left = mine_filed[x + 1][y - 1];
		bottom_left_exists = 1;
	}
	
	if (y > 0) {
		count_left = mine_filed[x][y - 1];
		left_exists = 1;
	}
	
	if ((x > 0) && (y > 0)) {
		count_top_left = mine_filed[x - 1][y - 1];
		top_left_exists = 1;
	}

	result_filed[x][y] = count_top + count_top_right + count_right + count_bottom_right + count_bottom + count_bottom_left + count_left + count_top_left;
	
//	printf("result_filed[%d][%d] = %d\t", x, y, result_filed[x][y]);
//	printf("(%d %d %d %d %d %d %d %d)\n", count_top, count_top_right, count_right, count_bottom_right, count_bottom, count_bottom_left, count_left, count_top_left);

	if (result_filed[x][y] == 0) {
		if (top_exists)
			count_mines(x - 1, y);

		if (top_right_exists)
			count_mines(x - 1, y + 1);

		if (right_exists)
			count_mines(x, y + 1);

		if (bottom_right_exists)
			count_mines(x + 1, y + 1);
	
		if (bottom_exists)
			count_mines(x + 1, y);
	
		if (bottom_left_exists)
			count_mines(x - 1, y + 1);
	
		if (left_exists)
			count_mines(x, y - 1);
	
		if (top_left_exists) 
			count_mines(x - 1, y - 1);
	}
}

int main () {
	int x, y, i, j;

	fill_results();

	printf("Enter row, col: ");
	scanf("%d, %d", &x, &y);
	printf("row=%d, col=%d\n", x, y);

	print_matrix(mine_filed, x, y);

	count_mines (x, y);

	print_matrix(result_filed, x, y);

	return (0);
}