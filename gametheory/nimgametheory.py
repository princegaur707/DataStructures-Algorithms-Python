'''
“ Given a number of piles in which each pile contains some numbers of stones/coins.
In each turn, a player can choose only one pile and remove any number of stones (at least one) from that pile.
The player who cannot move is considered to lose the game (i.e., one who take the last stone is the winner). ”
“If both Alice and Bob play optimally (i.e.- they don’t make any mistakes),
then the player starting first is guaranteed to win if the Nim-Sum at the beginning of the game is non-zero.
Otherwise, if the Nim-Sum evaluates to zero, then player Alice will lose definitely.'''
def getNimSum(arr,n):
    res = arr[0]
    for i in range(1,n):
        res = res^arr[i]
    return res

t = int(input())
