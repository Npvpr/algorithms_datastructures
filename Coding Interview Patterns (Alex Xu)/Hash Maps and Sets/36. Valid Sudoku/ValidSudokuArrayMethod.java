import java.util.HashSet;

// More Verbose method
public class ValidSudokuArrayMethod {
    public static void main(String[] args) {
        System.out.println(solution(new char[][] { { '5', '3', '.', '.', '7', '.', '.', '.', '.' },
                { '6', '.', '.', '1', '9', '5', '.', '.', '.' }, { '.', '9', '8', '.', '.', '.', '.', '6', '.' },
                { '8', '.', '.', '.', '6', '.', '.', '.', '3' }, { '4', '.', '.', '8', '.', '3', '.', '.', '1' },
                { '7', '.', '.', '.', '2', '.', '.', '.', '6' }, { '.', '6', '.', '.', '.', '.', '2', '8', '.' },
                { '.', '.', '.', '4', '1', '9', '.', '.', '5' }, { '.', '.', '.', '.', '8', '.', '.', '7', '9' } }));
        System.out.println(solution(new char[][] { { '8', '3', '.', '.', '7', '.', '.', '.', '.' },
                { '6', '.', '.', '1', '9', '5', '.', '.', '.' }, { '.', '9', '8', '.', '.', '.', '.', '6', '.' },
                { '8', '.', '.', '.', '6', '.', '.', '.', '3' }, { '4', '.', '.', '8', '.', '3', '.', '.', '1' },
                { '7', '.', '.', '.', '2', '.', '.', '.', '6' }, { '.', '6', '.', '.', '.', '.', '2', '8', '.' },
                { '.', '.', '.', '4', '1', '9', '.', '.', '5' }, { '.', '.', '.', '.', '8', '.', '.', '7', '9' } }));
        // int[] nArr = new int[] {1,2,3,4};
        // int[][] nTArr = new int[][] {{1,2}, {3,4}};
    }

    public static boolean solution(char[][] board) {
        // The board size must always be 9x9
        HashSet<Character>[] rows = new HashSet[9];
        HashSet<Character>[] cols = new HashSet[9];
        HashSet<Character>[][] grids = new HashSet[3][3];

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {

                if (rows[r] == null)
                    rows[r] = new HashSet<>();
                if (cols[c] == null)
                    cols[c] = new HashSet<>();
                if (grids[r / 3][c / 3] == null)
                    grids[r / 3][c / 3] = new HashSet<>();

                char num = board[r][c];
                if (num != '.') {
                    if (rows[r].contains(num) || cols[c].contains(num) || grids[r / 3][c / 3].contains(num)) {
                        return false;
                    }
                    rows[r].add(num);
                    cols[c].add(num);
                    grids[r / 3][c / 3].add(num);
                }
            }
        }

        return true;
    }
}
