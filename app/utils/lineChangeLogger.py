def line_change_logger(recourds):
    for i in range(len(recourds)):
        prevLine = recourds[i]["lines"][0]
        for j in range(len(recourds[i]["lines"])):
            if recourds[i]["lines"][j] != prevLine:
                currentLine = recourds[i]["lines"][j]
                recourds[i]["paths"].insert(j+(len(recourds[i]["paths"]) - len(recourds[i]["lines"])), {"type": "change_line",
                                                       "to": currentLine, "fa": f"تعویض خط به سمت خط {currentLine}"})
            prevLine = recourds[i]["lines"][j]

    return recourds
