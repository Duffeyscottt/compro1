import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.Location = System.Drawing.Point(12, 217)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(353, 135)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "groupBox1"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PeachPuff
        self._button1.ForeColor = System.Drawing.Color.SaddleBrown
        self._button1.Location = System.Drawing.Point(41, 380)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(93, 39)
        self._button1.TabIndex = 1
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = False
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.PeachPuff
        self._button2.ForeColor = System.Drawing.Color.SaddleBrown
        self._button2.Location = System.Drawing.Point(140, 380)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(93, 39)
        self._button2.TabIndex = 2
        self._button2.Text = "button2"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.PeachPuff
        self._button3.ForeColor = System.Drawing.Color.SaddleBrown
        self._button3.Location = System.Drawing.Point(239, 380)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(93, 39)
        self._button3.TabIndex = 3
        self._button3.Text = "button3"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.SeaShell
        self.ClientSize = System.Drawing.Size(377, 431)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "Pg269Race"
        self.ResumeLayout(False)

