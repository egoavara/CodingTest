package Programmers.C30L1829;

import java.util.*;

class Solution {
    public static void main(String[] args) {
        int[][] ex = { { 1, 0, 0, 1 }, { 1, 0, 1, 1 }, { 1, 0, 0, 1 }, { 1, 0, 1, 1 }, { 1, 0, 0, 1 }, { 1, 1, 1, 1 } };
        int[] result = solution(6, 4, ex);
        System.out.println(result[0]);
        System.out.println(result[1]);
    }

    public static int[] solution(int m, int n, int[][] picture) {
        int[][] cpic = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cpic[i][j] = picture[i][j];
            }
        }
        int[] result = new int[2];
        int max = 1;
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (cpic[i][j] != 0) {
                    count++;
                    int t = cpic[i][j];
                    cpic[i][j] = 0;
                    int tmp = bfs(cpic, i, j, t);
                    max = Math.max(max, tmp);
                }
            }
        }

        result[0] = count;
        result[1] = max;
        return result;
    }

    public static int bfs(int[][] picture, int i, int j, int target) {
        int count = 1;
        int m = picture.length;
        int n = picture[0].length;
        int[][] dirs = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] { i, j });
        while (!queue.isEmpty()) {
            int[] xy = queue.poll();
            for (int[] dir : dirs) {
                int x = xy[0] + dir[0];
                int y = xy[1] + dir[1];
                if (x >= 0 && x < m && y >= 0 && y < n && picture[x][y] == target) {
                    count++;
                    picture[x][y] = 0;
                    queue.offer(new int[] { x, y });
                }
            }
        }
        return count;
    }
}