public class SetMatrixZeroes {
    // Time Complexity: O(m x n)
    // Alex Xu's HashSet method cost Space Complexity: O(m + n)
    // But this Neetcode's method cost Space Complexity: O(1)
    public static void main(String[] args) {
        System.out.println(solution(new int[][] { { 1, 1, 1 }, { 1, 0, 1 }, { 1, 1, 1 } }));
        System.out.println(solution(new int[][] { { 0, 1, 2, 0 }, { 3, 4, 5, 2 }, { 1, 3, 1, 5 } }));
    }

    public static int[][] solution(int[][] matrix) {
        int rlen = matrix.length;
        int clen = matrix[0].length;
        int rZero = matrix[0][0];

        for (int r = 0; r < rlen; r++) {
            for (int c = 0; c < clen; c++) {
                if (matrix[r][c] == 0) {
                    if (r == 0) {
                        rZero = 0;
                    } else {
                        matrix[r][0] = 0;
                    }
                    matrix[0][c] = 0;
                }
            }
        }

        for (int r = 1; r < rlen; r++) {
            for (int c = 1; c < clen; c++) {
                if (matrix[r][0] == 0 || matrix[0][c] == 0) {
                    matrix[r][c] = 0;
                }
            }
        }

        if (matrix[0][0] == 0) {
            for (int r = 0; r < rlen; r++) {
                matrix[r][0] = 0;
            }
        }

        if (rZero == 0) {
            for (int c = 0; c < clen; c++) {
                matrix[0][c] = 0;
            }
        }

        return matrix;
    }
}
