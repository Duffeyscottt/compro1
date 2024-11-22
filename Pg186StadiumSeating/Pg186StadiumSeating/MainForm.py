import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
        self._groupBox1.Font = System.Drawing.Font("Gill Sans MT Condensed", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.ForeColor = System.Drawing.Color.Red
        self._groupBox1.Location = System.Drawing.Point(12, 12)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(285, 216)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Tickets Sold"
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
        self._groupBox2.Font = System.Drawing.Font("Gill Sans MT Condensed", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.ForeColor = System.Drawing.Color.Red
        self._groupBox2.Location = System.Drawing.Point(320, 12)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.RightToLeft = System.Windows.Forms.RightToLeft.Yes
        self._groupBox2.Size = System.Drawing.Size(285, 216)
        self._groupBox2.TabIndex = 1
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Revenue Generated"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LimeGreen
        self.ClientSize = System.Drawing.Size(617, 331)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "Pg186StadiumSeating"
        self.ResumeLayout(False)

