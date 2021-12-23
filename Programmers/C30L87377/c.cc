#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// linerows는 2차원 배열 line의 행 길이, linecols는 2차원 배열 line의 열
// 길이입니다.
char** solution(int** line, size_t line_rows, size_t line_cols) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게
    // 변경해주세요.
    float x, y, xnmg, ynmg = 0;
    int parel, count = 0;
    int** arr;
    int size = 0;
    int minr, minc, maxr, maxc = 0;
    int ansrow, anscol = 0;
    float xzero, yzero = 0;

    // for (int i = 0; i < line_rows - 1; i++) {
    //     size = size + (line_rows - 1) - i;
    // }

    // printf("-%d\n", size);
    // arr = (int**)malloc(sizeof(int*) * size);
    // for (int i = 0; i < size; i++) {
        
    //     printf("--\n");
    //     arr[i] = (int*)malloc(sizeof(int) * 2);
    // }

    // for (int i = 0; i < line_rows; i++) {
    //     for (int j = i + 1; j < line_rows; j++) {
    //         parel =
    //             (float)(line[i][0] * line[j][1]) - (line[i][1] * line[j][0]);
    //         if (parel == 0) {
    //             continue;
    //         } else {
    //             xzero = ((line[i][1] * line[j][2]) - (line[i][2] * line[j][1]));
    //             yzero = ((line[i][2] * line[j][0]) - (line[i][0] * line[j][2]));
    //             if (xzero == 0) {
    //                 x = 0;
    //             } else {
    //                 x = parel / xzero;
    //             }
    //             if (yzero == 0) {
    //                 y = 0;
    //             } else {
    //                 y = parel / yzero;
    //             }

    //             xnmg = fmod(x, 1.0);
    //             ynmg = fmod(y, 1.0);

    //             if (xnmg == 0.0 && ynmg == 0.0) {
    //                 arr[count][0] = (int)x;
    //                 arr[count][1] = (int)y;
    //                 count++;
    //             }
    //         }
    //     }
    // }
    // arr = (int**)realloc(arr, count * sizeof(int));

    // minr = arr[0][1];
    // minc = arr[0][0];
    // maxr = arr[0][1];
    // maxc = arr[0][0];
    // for (int i = 0; i < count; i++) {
    //     if (arr[i][1] < minr) {
    //         minr = arr[i][1];
    //     }
    //     if (arr[i][0] < minc) {
    //         minc = arr[i][0];
    //     }
    //     if (arr[i][1] > maxr) {
    //         maxr = arr[i][1];
    //     }
    //     if (arr[i][0] > maxc) {
    //         maxc = arr[i][0];
    //     }
    // }

    // ansrow = maxr - minr;
    // if (ansrow < 0) {
    //     ansrow = (-1) * ansrow;
    // }
    // anscol = maxc - minc;
    // if (anscol < 0) {
    //     anscol = (-1) * anscol;
    // }

    // if (minr < 0) {
    //     for (int i = 0; i < count; i++) {
    //         arr[i][1] = arr[i][1] + ((-1) * minr);
    //     }
    // }
    // if (minc < 0) {
    //     for (int i = 0; i < count; i++) {
    //         arr[i][0] = arr[i][0] + ((-1) * minc);
    //     }
    // }
    // if (minr > 0) {
    //     for (int i = 0; i < count; i++) {
    //         arr[i][1] = arr[i][1] - minr;
    //     }
    // }
    // if (minc > 0) {
    //     for (int i = 0; i < count; i++) {
    //         arr[i][0] = arr[i][0] - minc;
    //     }
    // }

    char** answer = (char**)malloc(100);
    // answer = (char**)malloc((ansrow + 1) * sizeof(char*));
    // for (int i = 0; i < (ansrow + 1); i++) {
    //     answer[i] = (char*)malloc(sizeof(char) * (anscol + 1));
    // }

    // for (int i = 0; i < ansrow + 1; i++) {
    //     for (int j = 0; j < anscol + 1; j++) {
    //         answer[i][j] = '.';
    //     }
    // }

    // for (int i = 0; i < count; i++) {
    //     answer[arr[i][1]][arr[i][0]] = '*';
    // }

    return answer;
}