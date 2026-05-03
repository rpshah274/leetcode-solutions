# Problem: Word Search
# URL: https://leetcode.com/problems/word-search/
# Language: cpp

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        int n = board[0].size();

        function<bool(int,int,int)> solve = [&](int i, int j, int idx) -> bool {
            if (idx == word.size()) return true;
            if (i < 0 || j < 0 || i >= m || j >= n || board[i][j] == '#' || board[i][j] != word[idx]) {
                return false;
            }

            char temp = board[i][j];
            board[i][j] = '#';

            bool ans = solve(i + 1, j, idx + 1) ||
                       solve(i - 1, j, idx + 1) ||
                       solve(i, j + 1, idx + 1) ||
                       solve(i, j - 1, idx + 1);

            board[i][j] = temp;
            return ans;
        };

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word[0] && solve(i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
};