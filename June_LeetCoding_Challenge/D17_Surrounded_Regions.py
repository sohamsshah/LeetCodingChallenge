# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:04:06 2020

@author: Soham Shah
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        nb_row = len(board)
        nb_col = len(board[0]) if board else 0

        def helper(board, i: int, j: int) -> None:
            if i >= 0 and i < nb_row and j >= 0 and j < nb_col:
                if board[i][j] == 'O':
                    board[i][j] = 'D'
                    helper(board, i + 1, j)
                    helper(board, i - 1, j)
                    helper(board, i, j + 1)
                    helper(board, i, j - 1)
                    
        # change left and right border O into D
        for row in range(nb_row):
            helper(board, row, 0)
            helper(board, row, nb_col - 1)
        
        # change up and down border O into D
        for col in range(nb_col):
            helper(board, 0, col)
            helper(board, nb_row - 1, col)

        for row in range(nb_row):
            for col in range(nb_col):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'D':
                    board[row][col] = 'O'