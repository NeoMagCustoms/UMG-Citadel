const fs = require('fs');
const path = require('path');

const masterFile = path.join(__dirname, '..', 'incoming_master', 'category_27_payment_billing_blocks.json');
const incomingRoot = path.join(__dirname, '..', 'incoming');

function ensureDir(dir) {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

const blocks = JSON.parse(fs.readFileSync(masterFile, 'utf8'));

blocks.forEach((block) => {
  const categoryPath = block.category.replace(/^\/+|\/+$/g, '');
  const targetDir = path.join(incomingRoot, categoryPath);
  ensureDir(targetDir);

  const outPath = path.join(targetDir, `${block.block_id}.json`);
    if (fs.existsSync(outPath)) {
    console.warn('File already exists, skipping:', outPath);
    return;
  }

  fs.writeFileSync(outPath, JSON.stringify(block, null, 2));
  console.log('Wrote', outPath);
});
