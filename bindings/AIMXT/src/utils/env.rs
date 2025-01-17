use std::collections::HashMap;
use std::fs::File;
use std::io::Write;
pub(crate) fn write_to_env_file(env_vars: &HashMap<&str, String>) -> std::io::Result<()> {
    let mut file = File::create(".AIMXT_network")?;

    for (key, value) in env_vars {
        writeln!(file, "{}={}", key, value)?;
    }

    Ok(())
}