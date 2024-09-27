import System.Drawing
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
        self._button4 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Orange
        self._button1.Font = System.Drawing.Font("Palatino Linotype", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.White
        self._button1.Location = System.Drawing.Point(-1, 249)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(184, 28)
        self._button1.TabIndex = 0
        self._button1.Text = "last name"
        self._button1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Orange
        self._button2.Font = System.Drawing.Font("Palatino Linotype", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.White
        self._button2.Location = System.Drawing.Point(179, 249)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(184, 28)
        self._button2.TabIndex = 1
        self._button2.Text = "first name"
        self._button2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Orange
        self._button3.Font = System.Drawing.Font("Palatino Linotype", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.White
        self._button3.Location = System.Drawing.Point(359, 249)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(184, 28)
        self._button3.TabIndex = 2
        self._button3.Text = "clear"
        self._button3.TextAlign = System.Drawing.ContentAlignment.TopCenter
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.Color.Orange
        self._button4.Font = System.Drawing.Font("Palatino Linotype", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.ForeColor = System.Drawing.Color.White
        self._button4.Location = System.Drawing.Point(539, 249)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(184, 28)
        self._button4.TabIndex = 3
        self._button4.Text = "exit"
        self._button4.TextAlign = System.Drawing.ContentAlignment.TopCenter
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Stencil", 130, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Orange
        self._label1.Location = System.Drawing.Point(-1, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(724, 191)
        self._label1.TabIndex = 4
        self._label1.Text = "DUFFEY"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Stencil", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Orange
        self._label2.Location = System.Drawing.Point(-1, 162)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(724, 21)
        self._label2.TabIndex = 5
        self._label2.Text = "shannon"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Orange
        self.ClientSize = System.Drawing.Size(722, 276)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "PhoneNumbers"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.ForeColor = System.Drawing.Color.Black

    def Button2Click(self, sender, e):
        self._label2.ForeColor = System.Drawing.Color.Black

    def Button3Click(self, sender, e):
        self._label2.ForeColor = System.Drawing.Color.Orange
        self._label1.ForeColor = System.Drawing.Color.Orange

    def Button4Click(self, sender, e):
        Application.Exit()