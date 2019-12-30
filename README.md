# hw_crawler
計概python爬蟲
組員：B08902007 呂以恩 B08902015 黃竑鈞 B08902023 吳懷兟

執行前請先執行
pip freeze > requirements.txt

執行主程式
python main.py --start-date 起始日期 --end-date 結束日期 --output 輸出位置

e.g. python3 main.py --start-date 2019-12-02 --end-date  2019-12-22 --output  output1.csv

這會輸出一個包含所有在資工系網站公告欄的所有在日期範圍內的消息到輸出檔案（預設為output.csv），格式為 日期|標題|內容，--start-date及--end-date為必要參數