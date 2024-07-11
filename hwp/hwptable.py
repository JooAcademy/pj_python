# -*- coding: utf-8 -*-
'''
import win32com.client as win32

hwp = win32.Dispatch("HWPFrame.HwpObject")
hwp.XHwpWindows.Item(0).Visible = True

# 5 X 4 테이블 만들기
row = 5
col = 4
tbl = hwp.CreateAction("TableCreate")
tblset = tbl.CreateSet()
tbl.GetDefault(tblset)
tblset.SetItem("Rows", row)
tblset.SetItem("Cols", col)
tbl.Execute(tblset)

# 테이블 셀 블록 선택
hwp.Run("TableCellBlock")
hwp.Run("tableCellBlockExtend")

for c in range(1, col):
    hwp.Run("TableRightCell")
    
for r in range(1, row):
    hwp.Run("TableLowerCell")
    
# 테이블 셀 크기 변경    
for k in range(12):
    hwp.Run("TableResizeRight")
for k in range(3):
    hwp.Run("TableResizeDown")
    
hwp.Run("Cancel");

# 테이블의 첫번째 셀로 이동
for c in range(1, col):
    hwp.Run("MoveLeft")
    
for r in range(1, row):
    hwp.Run("MoveUp")
    
# 테이블 제목 배경 색 지정
for c in range(col):
    hwp.HAction.GetDefault("CellFill", hwp.HParameterSet.HCellBorderFill.HSet)
    hwp.HParameterSet.HCellBorderFill.FillAttr.type = hwp.BrushType("NullBrush|WinBrush")
    hwp.HParameterSet.HCellBorderFill.FillAttr.WinBrushFaceColor = hwp.RGBColor(220, 220, 220)
    hwp.HParameterSet.HCellBorderFill.FillAttr.WinBrushHatchColor = hwp.RGBColor(153, 153, 153)
    hwp.HParameterSet.HCellBorderFill.FillAttr.WinBrushFaceStyle = hwp.HatchStyle("None")
    hwp.HParameterSet.HCellBorderFill.FillAttr.WindowsBrush = 1
    hwp.HAction.Execute("CellFill", hwp.HParameterSet.HCellBorderFill.HSet)
    hwp.HAction.Run("TableRightCell")
    
for c in range(col):
    hwp.Run("MoveLeft")

# 테이블에 텍스트 넣기
for r in range(row):
    for c in range(col):
        hwp.HParameterSet.HInsertText.Text = f'({r}, {c})'
        hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)
        hwp.Run("MoveRight")

'''

# -*- coding: utf-8 -*-

import win32com.client as win32
import time  # 지연시간 추가를 위해 time 모듈 임포트

hwp = win32.Dispatch("HWPFrame.HwpObject")
hwp.XHwpWindows.Item(0).Visible = True

# 5 X 4 테이블 만들기
row = 5
col = 4
tbl = hwp.CreateAction("TableCreate")
tblset = tbl.CreateSet()
tbl.GetDefault(tblset)
tblset.SetItem("Rows", row)
tblset.SetItem("Cols", col)
tbl.Execute(tblset)

# 테이블 셀 블록 선택
hwp.Run("TableCellBlock")
hwp.Run("tableCellBlockExtend")

for c in range(1, col):
    hwp.Run("TableRightCell")
    time.sleep(0.5)  # 지연 시간 추가
    
for r in range(1, row):
    hwp.Run("TableLowerCell")
    time.sleep(0.5)  # 지연 시간 추가
    
# 테이블 셀 크기 변경    
for k in range(12):
    hwp.Run("TableResizeRight")
    time.sleep(0.5)  # 지연 시간 추가
    
for k in range(3):
    hwp.Run("TableResizeDown")
    time.sleep(0.5)  # 지연 시간 추가
    
hwp.Run("Cancel")

# 테이블의 첫번째 셀로 이동
for c in range(1, col):
    hwp.Run("MoveLeft")
    time.sleep(0.5)  # 지연 시간 추가
    
for r in range(1, row):
    hwp.Run("MoveUp")
    time.sleep(0.5)  # 지연 시간 추가
    
# 테이블 제목 배경 색 지정
for c in range(col):
    hwp.HAction.GetDefault("CellFill", hwp.HParameterSet.HCellBorderFill.HSet)
    hwp.HParameterSet.HCellBorderFill.FillAttr.type = hwp.BrushType("NullBrush|WinBrush")
    hwp.HParameterSet.HCellBorderFill.FillAttr.WinBrushFaceColor = hwp.RGBColor(220, 220, 220)
    hwp.HParameterSet.HCellBorderFill.FillAttr.WinBrushHatchColor = hwp.RGBColor(153, 153, 153)
    hwp.HParameterSet.HCellBorderFill.FillAttr.WinBrushFaceStyle = hwp.HatchStyle("None")
    hwp.HParameterSet.HCellBorderFill.FillAttr.WindowsBrush = 1
    hwp.HAction.Execute("CellFill", hwp.HParameterSet.HCellBorderFill.HSet)
    hwp.HAction.Run("TableRightCell")
    time.sleep(0.5)  # 지연 시간 추가
    
for c in range(col):
    hwp.Run("MoveLeft")
    time.sleep(0.5)  # 지연 시간 추가

# 테이블에 텍스트 넣기
for r in range(row):
    for c in range(col):
        hwp.HParameterSet.HInsertText.Text = f'({r}, {c})'
        hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)
        time.sleep(0.5)  # 지연 시간 추가
        hwp.Run("MoveRight")
