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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Coral
        self._button1.Font = System.Drawing.Font("Lucida Bright", 11, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 331)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(153, 36)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Coral
        self._button2.Font = System.Drawing.Font("Lucida Bright", 11, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(171, 331)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(153, 36)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Coral
        self._button3.Font = System.Drawing.Font("Lucida Bright", 11, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(330, 331)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(153, 36)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(144, 13)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(341, 46)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(144, 74)
        self._textBox2.Multiline = True
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(341, 46)
        self._textBox2.TabIndex = 4
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Coral
        self._label1.Font = System.Drawing.Font("Lucida Bright", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(126, 46)
        self._label1.TabIndex = 5
        self._label1.Text = "Total:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Coral
        self._label2.Font = System.Drawing.Font("Lucida Bright", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 74)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(126, 46)
        self._label2.TabIndex = 6
        self._label2.Text = "Paid:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Coral
        self._label3.Font = System.Drawing.Font("Lucida Bright", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 139)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(126, 46)
        self._label3.TabIndex = 7
        self._label3.Text = "Change:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.MistyRose
        self._label4.Font = System.Drawing.Font("Lucida Bright", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(144, 139)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(97, 26)
        self._label4.TabIndex = 8
        self._label4.Text = "Dollars:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.MistyRose
        self._label5.Font = System.Drawing.Font("Lucida Bright", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(144, 177)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(97, 26)
        self._label5.TabIndex = 9
        self._label5.Text = "Quarters:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.MistyRose
        self._label6.Font = System.Drawing.Font("Lucida Bright", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(144, 253)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(97, 26)
        self._label6.TabIndex = 11
        self._label6.Text = "Nickles:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.MistyRose
        self._label7.Font = System.Drawing.Font("Lucida Bright", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(144, 215)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(97, 26)
        self._label7.TabIndex = 10
        self._label7.Text = "Dimes:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.MistyRose
        self._label8.Font = System.Drawing.Font("Lucida Bright", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(144, 290)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(97, 26)
        self._label8.TabIndex = 12
        self._label8.Text = "Pennies:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.LightSalmon
        self._label9.Font = System.Drawing.Font("Lucida Bright", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(247, 290)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(134, 26)
        self._label9.TabIndex = 17
        self._label9.Text = " "
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.LightSalmon
        self._label10.Font = System.Drawing.Font("Lucida Bright", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(247, 253)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(134, 26)
        self._label10.TabIndex = 16
        self._label10.Text = " "
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.LightSalmon
        self._label11.Font = System.Drawing.Font("Lucida Bright", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(247, 215)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(134, 26)
        self._label11.TabIndex = 15
        self._label11.Text = " "
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.LightSalmon
        self._label12.Font = System.Drawing.Font("Lucida Bright", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(247, 177)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(134, 26)
        self._label12.TabIndex = 14
        self._label12.Text = " "
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.LightSalmon
        self._label13.Font = System.Drawing.Font("Lucida Bright", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(247, 139)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(134, 26)
        self._label13.TabIndex = 13
        self._label13.Text = " "
        self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.Coral
        self._label14.Font = System.Drawing.Font("Lucida Bright", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.Location = System.Drawing.Point(12, 207)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(126, 109)
        self._label14.TabIndex = 18
        self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Sienna
        self.ClientSize = System.Drawing.Size(497, 382)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog58t"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._textBox1.Text = " "
        self._textBox2.Text = " "
        self._label9.Text = " "
        self._label10.Text = " "
        self._label11.Text = " "
        self._label12.Text = " "
        self._label13.Text = " "
        self._label14.Text = " "

    def Button1Click(self, sender, e):
        total = float(self._textBox1.Text)
        paid = float(self._textBox2.Text)
        if total > paid:
            self._label14.Text = "Invalid payment amount."
        elif total == paid:
            self._label14.Text = "No change to be given."
        elif total < paid:
            change = paid - total
            dollars = change // 1
            self._label13.Text = str(dollars)
            cents = change % 1 * 100
            cents = round(cents, 2)
            quarters = cents // 25
            centsminuquar = cents % 25
            dimes = centsminuquar // 10
            centsminudime = centsminuquar % 10
            nickles = centsminudime // 5
            pennies = centsminudime % 5
            self._label12.Text = str(quarters)
            self._label11.Text = str(dimes)
            self._label10.Text = str(nickles)
            self._label9.Text = str(pennies)
