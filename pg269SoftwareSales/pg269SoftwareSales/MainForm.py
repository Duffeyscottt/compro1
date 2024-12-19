import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(12, 29)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Package A:"
        # 
        # groupBox1
        # 
        self._groupBox1.Controls.Add(self._label3)
        self._groupBox1.Controls.Add(self._label2)
        self._groupBox1.Controls.Add(self._label1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 11, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(23, 12)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(261, 133)
        self._groupBox1.TabIndex = 1
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Quantity Sold"
        # 
        # groupBox2
        # 
        self._groupBox2.Location = System.Drawing.Point(12, 151)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(161, 89)
        self._groupBox2.TabIndex = 2
        self._groupBox2.TabStop = False
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(199, 162)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 29)
        self._button1.TabIndex = 3
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(179, 197)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(55, 29)
        self._button2.TabIndex = 4
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(240, 197)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(55, 29)
        self._button3.TabIndex = 5
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(12, 89)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Package C:"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(12, 59)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "Package B:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(307, 252)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "pg269SoftwareSales"
        self._groupBox1.ResumeLayout(False)
        self.ResumeLayout(False)

