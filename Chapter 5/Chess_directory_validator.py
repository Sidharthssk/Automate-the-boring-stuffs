def isValidChessBoard(chessboard):
    wpieces={}
    bpieces={}
    piece=['pawn','knight','bishop','rook','queen','king']
    letter = ['a','b','c','d','e','f','g','h']
    dig=['1','2','3','4','5','6','7','8']
    total_white=0;
    total_black=0

    for i in chessboard.values():
        if i[0]=='w':
            wpieces.setdefault(i,0)
            wpieces[i]+=1
        elif i[0]=='b':
            bpieces.setdefault(i,0)
            bpieces[i]+=1

    if (wpieces.get('wking',0)!=1) and (bpieces.get('bking',0)!=1):
        print('Invalid number of king')
        return False

    for i in wpieces.values():
        total_white+=i
    for i in bpieces.values():
        total_black+=i
    if total_black>16 or total_white>16:
        print("invalid number of pieces")
        return False

    if (wpieces.get('wpawns',0)>8) or (bpieces.get('bpawns',0)>8):
       print('Invalid number of pawns present')
       return False

    for i in chessboard.keys():
      if i[0] not in dig:
          print('Invalid square ')
          return False
      if i[1] not in letter:
          print('Invalid square ')
          return False


    for i in chessboard.values():
        if(i[0]!='w' and i[0]!='b'):
            print('Invalid color ')
            return False

    for i in chessboard.values():
        if i[1:] not in piece:
            print('Invlid piece present on the board')
            return False

    return True

board = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
'5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn'
}

if(isValidChessBoard(board)):
    print('It is a valid chess board')
else :
    print('Invalid chess board')
