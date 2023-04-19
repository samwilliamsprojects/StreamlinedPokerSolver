remove_file() {
rm ouput_result.json
}
[[ $(remove_file  2>&1) =~ "No such file" ]]
cd TexasSolver-v0.2.0-MacOs
./console_solver -i input.txt 
