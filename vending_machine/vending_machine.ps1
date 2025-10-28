# ===============================
# VendingMachine Coverage Script
# ===============================

# 1️⃣ Clean old outputs
Write-Host "Cleaning old files..."
Remove-Item -Recurse -Force out, report, jacoco.exec -ErrorAction SilentlyContinue
New-Item -ItemType Directory out | Out-Null
New-Item -ItemType Directory ..\tools -ErrorAction SilentlyContinue | Out-Null

# 2️⃣ Ensure JaCoCo JARs exist
$agentPath = "..\tools\jacocoagent.jar"
$cliPath = "..\tools\jacoco-cli.jar"
if (-Not (Test-Path $agentPath)) {
    Write-Host "Downloading JaCoCo agent..."
    Invoke-WebRequest -Uri "https://repo1.maven.org/maven2/org/jacoco/org.jacoco.agent/0.8.12/org.jacoco.agent-0.8.12-runtime.jar" -OutFile $agentPath
}
if (-Not (Test-Path $cliPath)) {
    Write-Host "Downloading JaCoCo CLI..."
    Invoke-WebRequest -Uri "https://repo1.maven.org/maven2/org/jacoco/org.jacoco.cli/0.8.12/org.jacoco.cli-0.8.12-nodeps.jar" -OutFile $cliPath
}

# 3️⃣ Compile Java sources into ./out
Write-Host "Compiling Java files..."
javac -g -d out -cp ".;lib\junit-platform-console-standalone-1.10.1.jar" VendingMachine.java VendingMachineTest.java
if ($LASTEXITCODE -ne 0) { Write-Error "Compilation failed!"; exit 1 }

# 4️⃣ Run tests with JaCoCo agent
Write-Host "Running tests with JaCoCo agent..."
java -javaagent:$agentPath=destfile=jacoco.exec,append=false,includes=VendingMachine* `
     -jar lib\junit-platform-console-standalone-1.10.1.jar `
     -cp "out" --select-class VendingMachineTest
if ($LASTEXITCODE -ne 0) { Write-Error "Test execution failed!"; exit 1 }

# 5️⃣ Generate HTML coverage report
Write-Host "Generating HTML coverage report..."
java -jar $cliPath report jacoco.exec --classfiles out\VendingMachine.class --sourcefiles . --html report
if ($LASTEXITCODE -ne 0) { Write-Error "Failed to generate report!"; exit 1 }

# 6️⃣ Done
Write-Host "`n✅ Coverage report generated: ./report/index.html"
