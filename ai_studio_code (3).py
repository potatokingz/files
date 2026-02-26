import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_alkali_sheet():
    # 1. Setup the figure and axis
    # A4-ish ratio, high DPI for crisp text
    fig, ax = plt.subplots(figsize=(10, 14), dpi=100)
    
    # Remove axes (we want a blank sheet)
    ax.axis('off')
    
    # Set limits to standard 0-1 coordinates for easy placement
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # --- CONSTANTS FOR LAYOUT ---
    title_y = 0.95
    elements_y = 0.82
    general_y = 0.65
    reactions_y = 0.40
    notes_y = 0.10
    
    left_margin = 0.05
    line_spacing = 0.035

    # --- TITLE ---
    ax.text(0.5, title_y, "Алкални метали (IA група)", 
            ha='center', va='center', fontsize=24, fontweight='bold', color='darkblue')
    ax.text(0.5, title_y - 0.04, "Li, Na, K, Rb, Cs, Fr", 
            ha='center', va='center', fontsize=16, color='gray')

    # Draw a line under title
    line = patches.FancyArrowPatch((0.1, title_y - 0.07), (0.9, title_y - 0.07), 
                                   arrowstyle='-', color='black', linewidth=2)
    ax.add_patch(line)

    # --- SECTION 1: THE ELEMENTS (Table) ---
    ax.text(left_margin, elements_y + 0.05, "1. Елементи", fontsize=16, fontweight='bold', color='darkred')
    
    # Header
    headers = ["Знак", "Име (BG)", "Z", "Електронна конфигурация"]
    col_pos = [0.05, 0.20, 0.45, 0.60]
    
    for i, h in enumerate(headers):
        ax.text(col_pos[i], elements_y, h, fontsize=12, fontweight='bold')

    # Data
    elements = [
        ("Li", "Литий", "3", "[He] 2s¹"),
        ("Na", "Натрий", "11", "[Ne] 3s¹"),
        ("K", "Калий", "19", "[Ar] 4s¹"),
        ("Rb", "Рубидий", "37", "[Kr] 5s¹"),
        ("Cs", "Цезий", "55", "[Xe] 6s¹"),
        ("Fr", "Франций", "87", "[Rn] 7s¹")
    ]

    curr_y = elements_y - 0.04
    for el in elements:
        ax.text(col_pos[0], curr_y, el[0], fontsize=12, fontweight='bold')
        ax.text(col_pos[1], curr_y, el[1], fontsize=12)
        ax.text(col_pos[2], curr_y, el[2], fontsize=12)
        ax.text(col_pos[3], curr_y, el[3], fontsize=12, fontstyle='italic')
        curr_y -= line_spacing

    # --- SECTION 2: GENERAL PROPERTIES ---
    ax.text(left_margin, general_y, "2. Обща характеристика", fontsize=16, fontweight='bold', color='darkred')
    
    props = [
        "• Обща валентна конфигурация: ns¹",
        "• Степен на окисление: винаги +1",
        "• Прости вещества: Меки, сребристобели метали",
        "• Съхранение: Под петрол (силно реактивоспособни)",
        "• Атомен радиус: Расте от Li към Cs",
        "• Йонизационна енергия: Намалява от Li към Cs (стават по-активни)"
    ]
    
    curr_y = general_y - 0.04
    for p in props:
        ax.text(left_margin + 0.02, curr_y, p, fontsize=12)
        curr_y -= line_spacing

    # --- SECTION 3: CHEMICAL FORMULAS (Reactions) ---
    ax.text(left_margin, reactions_y + 0.05, "3. Химични свойства и формули", fontsize=16, fontweight='bold', color='darkred')
    ax.text(left_margin + 0.45, reactions_y + 0.05, "(M = Алкален метал)", fontsize=12, fontstyle='italic')

    # We use LaTeX formatting (r"$...$") for chemical formulas
    reactions = [
        ("Взаимодействие с Кислород (O₂)", r"$4M + O_2 \rightarrow 2M_2O$ (Основен оксид)"),
        ("   *Забележка:", "Li прави оксид ($Li_2O$), Na прави пероксид ($Na_2O_2$), K прави супероксид ($KO_2$)"),
        
        ("Взаимодействие с Водород (H₂)", r"$2M + H_2 \rightarrow 2MH$ (Йонни хидриди)"),
        
        ("Взаимодействие с Халогени (Cl₂, Br₂...)", r"$2M + Cl_2 \rightarrow 2MCl$ (Соли)"),
        
        ("Взаимодействие с Вода (H₂O) - Бурна реакция!", r"$2M + 2H_2O \rightarrow 2MOH + H_2 \uparrow$"),
        
        ("Взаимодействие с Киселини (напр. HCl)", r"$2M + 2HCl \rightarrow 2MCl + H_2 \uparrow$"),
        
        ("Свойства на хидроксидите (MOH)", "Силни основи (алкали). Дисоциират напълно:"),
        ("", r"$MOH \rightarrow M^+ + OH^-$"),
        
        ("Неутрализация (с киселини)", r"$MOH + HCl \rightarrow MCl + H_2O$")
    ]

    curr_y = reactions_y 
    for title, formula in reactions:
        if title:
            ax.text(left_margin + 0.02, curr_y, title, fontsize=11, fontweight='bold')
            # If there is a title, put formula slightly below or next to it? 
            # Let's put standard formulas on the next line for clarity
            if formula and not title.startswith("   *"):
                curr_y -= line_spacing
                ax.text(left_margin + 0.05, curr_y, formula, fontsize=14, color='blue')
            elif title.startswith("   *"):
                 # Note line
                 ax.text(left_margin + 0.20, curr_y, formula, fontsize=10, fontstyle='italic')
        else:
            # Just a formula continuation
            ax.text(left_margin + 0.05, curr_y, formula, fontsize=14, color='blue')
            
        curr_y -= (line_spacing * 1.5)

    # --- SECTION 4: FLAME COLORS ---
    # Draw a box for flame colors
    box_y = 0.12
    rect = patches.Rectangle((0.05, box_y), 0.9, 0.10, linewidth=1, edgecolor='gray', facecolor='#f9f9f9')
    ax.add_patch(rect)
    
    ax.text(0.5, box_y + 0.07, "Оцветяване на пламъка", ha='center', fontsize=12, fontweight='bold')
    
    flames = [
        ("Li: Карминовочервен", "red"),
        ("Na: Жълт", "#FFD700"), # Gold
        ("K: Виолетов", "purple"),
        ("Rb: Тъмночервен", "darkred"),
        ("Cs: Небесносин", "blue")
    ]
    
    # Distribute horizontally
    x_step = 0.18
    start_x = 0.07
    for i, (text, color) in enumerate(flames):
        ax.text(start_x + (i * x_step), box_y + 0.03, text.split(":")[0], 
                fontsize=12, fontweight='bold', color=color)
        ax.text(start_x + (i * x_step), box_y + 0.01, text.split(":")[1].strip(), 
                fontsize=9)

    # Footer
    ax.text(0.95, 0.01, "Generated with Python", ha='right', fontsize=8, color='lightgray')

    # Save
    filename = "alkalni_metali_sheet.png"
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.1)
    print(f"Successfully created: {filename}")
    
    # Optional: Show plot if running in a notebook
    # plt.show()

if __name__ == "__main__":
    generate_alkali_sheet()