import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightSteelBlue
        self._label1.Font = System.Drawing.Font("Franklin Gothic Medium Cond", 37, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Underline)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(347, 61)
        self._label1.TabIndex = 0
        self._label1.Text = "Phone Numbers"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.SlateGray
        self._button1.Font = System.Drawing.Font("Franklin Gothic Heavy", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.LightSteelBlue
        self._button1.ImageAlign = System.Drawing.ContentAlignment.TopCenter
        self._button1.Location = System.Drawing.Point(12, 73)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(56, 27)
        self._button1.TabIndex = 1
        self._button1.Text = "exit"
        self._button1.UseVisualStyleBackColor = False
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.SlateGray
        self._button2.Font = System.Drawing.Font("Franklin Gothic Heavy", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.LightSteelBlue
        self._button2.ImageAlign = System.Drawing.ContentAlignment.TopCenter
        self._button2.Location = System.Drawing.Point(12, 100)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(56, 27)
        self._button2.TabIndex = 2
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.SlateGray
        self._button3.Font = System.Drawing.Font("Franklin Gothic Heavy", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.LightSteelBlue
        self._button3.ImageAlign = System.Drawing.ContentAlignment.TopCenter
        self._button3.Location = System.Drawing.Point(12, 127)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(56, 27)
        self._button3.TabIndex = 3
        self._button3.Text = "show"
        self._button3.UseVisualStyleBackColor = False
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.LightSteelBlue
        self._label2.Font = System.Drawing.Font("Franklin Gothic Medium Cond", 30, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Underline)
        self._label2.ForeColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self._label2.Location = System.Drawing.Point(74, 73)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(285, 369)
        self._label2.TabIndex = 4
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.SlateGray
        self.ClientSize = System.Drawing.Size(371, 451)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "PhoneNumbers"
        self.ResumeLayout(False)





# numbers (608) 755-3015   (608) 580-0397   (608) 676-5569   (815) 965-3433   
