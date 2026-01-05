# from pyscript import document, display

from pyodide import create_proxy

        def compute_average(event):
            score1 = float(document.getElementById("score1").value)
            score2 = float(document.getElementById("score2").value)

            result_element = document.getElementById("result")
            
            
            if average >= 75:
                result_element.innerHTML = f"Average: {average} - Passed"
            else:
                result_element.innerHTML = f"Average: {average} - Failed"
        
        
        compute_button = document.getElementById("computeBtn")
        compute_button.addEventListener("click", create_proxy(compute_average))
