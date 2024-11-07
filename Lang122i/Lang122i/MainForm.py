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
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.AntiqueWhite
        self._listBox1.Font = System.Drawing.Font("Lucida Bright", 13, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 19
        self._listBox1.Location = System.Drawing.Point(12, 80)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(337, 346)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Moccasin
        self._button1.Font = System.Drawing.Font("Lucida Bright", 13, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(105, 62)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Moccasin
        self._button2.Font = System.Drawing.Font("Lucida Bright", 13, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(128, 12)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(105, 62)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Coral
        self._button3.Font = System.Drawing.Font("Lucida Bright", 13, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(244, 12)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(105, 62)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Tan
        self.ClientSize = System.Drawing.Size(361, 452)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "Lang122i"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        num = -26
        croot = 0
        cube = 0
        self._listBox1.Items.Add("Number\tCube Root   Cube")
        while num < 25:
            num = num + 1
            croot = num ** 1./3.
            cube = num ** 3
            croot = round(croot, 5)
            text = str(num) + "\t" + str(croot) + "\t    " + str(cube)
            self._listBox1.Items.Add(text)
            

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()
     

    def Button3Click(self, sender, e):
        Application.Exit()