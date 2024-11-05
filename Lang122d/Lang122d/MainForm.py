import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(12, 84)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(260, 160)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(12, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 23)
        self._button1.TabIndex = 1
        self._button1.Text = "button1"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(284, 261)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "Lang122d"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        x = -13
        y = 0
        while x < 16:
            x = x + 1
            y = x**6 - 3* x**5 - 93 * x**4 + 87 * x**3 + 1596 * x**2 - 1380 * x - 2800
            text = str(x) + " \t" + str(y)
            self._listBox1.Items.Add(text)
