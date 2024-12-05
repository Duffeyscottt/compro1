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
        self._label3 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(58, 7)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "label1"
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(58, 48)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "label2"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(58, 100)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "label3"
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(43, 174)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 23)
        self._button1.TabIndex = 3
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(124, 174)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(75, 23)
        self._button2.TabIndex = 4
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(205, 174)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(75, 23)
        self._button3.TabIndex = 5
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = True
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Location = System.Drawing.Point(164, 100)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(116, 23)
        self._label4.TabIndex = 6
        self._label4.Text = "label4"
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(164, 10)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(116, 20)
        self._textBox1.TabIndex = 7
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(164, 51)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(116, 20)
        self._textBox2.TabIndex = 8
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkCyan
        self.ClientSize = System.Drawing.Size(337, 209)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg268FatCalc"
        self.ResumeLayout(False)
        self.PerformLayout()

