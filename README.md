這個程式有三個for迴圈
最外的給每行query
第二個給source
最內的給每行query中的每一項
如果遇到and會從query的左而右搜尋，之間如果不符合就跳下一行source
如果遇到and會從query的左而右搜尋，之間如果符合就跳下一個query
如果遇到not會從query的左而右搜尋，如果沒有第一項會跳下一行source，之後的項如果存在也會跳下一行
