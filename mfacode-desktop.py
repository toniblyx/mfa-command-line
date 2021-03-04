#!/usr/bin/python

# MFA Authenticator for the command line
# This script gives a MFA code after 30 seconds from a given Secret key seed (QR code)

# Install pyotp (https://github.com/pyotp/pyotp) and wxPython as: 
# pip install pyotp wxpython
# Usage: python mfacode-desktop.py

import sys
import pyotp
import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='MFA Authenticator')
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        my_btn = wx.Button(panel, label='Generate MFA code')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
        panel.SetSizer(my_sizer)        
        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            #print("You didn't enter a secret seed!")
            wx.MessageBox("You didn't enter a secret seed!", '', 
                wx.OK | wx.ICON_ERROR)
        else:
            totp = pyotp.TOTP(value)
            dlg = wx.TextEntryDialog(None,"MFA code: ",'',totp.now())
            dlg.SetSize((320,180))
            if dlg.ShowModal() == wx.ID_OK:
                text = dlg.GetValue()
                print (text)
            dlg.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()