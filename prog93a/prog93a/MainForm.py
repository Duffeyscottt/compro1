﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Cyan
        self._button1.Font = System.Drawing.Font("Gill Sans Ultra Bold Condensed", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(96, 54)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Cyan
        self._button2.Font = System.Drawing.Font("Gill Sans Ultra Bold Condensed", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(12, 72)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(96, 54)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button3.Font = System.Drawing.Font("Gill Sans Ultra Bold Condensed", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(12, 132)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(96, 54)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label1.Font = System.Drawing.Font("Gill Sans MT", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(132, 12)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(277, 23)
        self._label1.TabIndex = 3
        self._label1.Text = "Enter KWH used"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # textBox1
        # 
        self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._textBox1.Location = System.Drawing.Point(240, 13)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(167, 20)
        self._textBox1.TabIndex = 4
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Gill Sans MT", 13)
        self._label2.Location = System.Drawing.Point(132, 39)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(277, 233)
        self._label2.TabIndex = 6
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self.ClientSize = System.Drawing.Size(421, 281)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Name = "MainForm"
        self.Text = "prog93a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._textBox1.Text = " "
        self._label2.Text = " "

    def Button1Click(self, sender, e):
        kwh = int(self._textBox1.Text)
        base = kwh * 0.0475
        base = round(base, 2)
        surcharge = base * 0.1
        surcharge = round(surcharge, 2)
        citytax = base * 0.03
        citytax = round(citytax, 2)
        total = base + citytax + surcharge
        total = round(total, 2)
        lateTotal = total * 1.04
        lateTotal = round(lateTotal, 2)
        #C O M P S C I Electric
#------------------------------------------------
#Kilowatts Used 993
#------------------------------------------------
#Base Rate 993 @ $ 0.0475 $ 47.17
#Surcharge $ 4.72
#Citytax $ 1.42
#______
#Pay this amount $ 53.31
#After May 20th Pay $ 55.44
        recipt = "C O M P S C I Electric" + "\nKilowatts used:   " + str(kwh) + "\nBase Rate   " \
        + str(kwh) + "* $ 0.0475   $" + str(base) + "\nSurcharge  $" + str(surcharge) + "\nCitytax   $" \
        + str(citytax) + "\n________" + "\nPay this amount   $" + str(total) + "\nAfter May 20th pay   $" +str(lateTotal)
        self._label2.Text = str(recipt)