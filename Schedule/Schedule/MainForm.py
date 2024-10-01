import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Stencil", 45, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.DarkSlateGray
        self._label1.Location = System.Drawing.Point(-1, -1)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(418, 95)
        self._label1.TabIndex = 0
        self._label1.Text = "Schedule"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Impact", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(66, 62)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(279, 345)
        self._label2.TabIndex = 1
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DarkTurquoise
        self._button1.Font = System.Drawing.Font("Impact", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.DarkSlateGray
        self._button1.Location = System.Drawing.Point(9, 410)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(130, 30)
        self._button1.TabIndex = 2
        self._button1.Text = "show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DarkTurquoise
        self._button2.Font = System.Drawing.Font("Impact", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.DarkSlateGray
        self._button2.Location = System.Drawing.Point(275, 410)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(130, 30)
        self._button2.TabIndex = 3
        self._button2.Text = "exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkTurquoise
        self._button3.Font = System.Drawing.Font("Impact", 14, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.DarkSlateGray
        self._button3.Location = System.Drawing.Point(142, 410)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(130, 30)
        self._button3.TabIndex = 4
        self._button3.Text = "clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkTurquoise
        self.ClientSize = System.Drawing.Size(413, 445)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Schedule"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        Application.Exit()

    def Button3Click(self, sender, e):
        self._label2.Text = " "

    def Button1Click(self, sender, e):
        self._label2.Text = "1st: P.E." + "\n 2nd: Computer Programming 1" + "\n 3rd: Chinese 3" + \
                            "\n 4th: Humanities A" + "\n 5th: English 11 Honors" + "\n 6th: AP PreCalc" + \
                            "\n 7th: Study Hall" + "\n 8th: AS Physics"